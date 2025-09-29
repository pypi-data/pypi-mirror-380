#!/usr/bin/env python3
"""
Generate Certificates Using mcp_security_framework with Bugfix
This script generates all necessary SSL certificates using the mcp_security_framework
with the CertificateConfig bugfix applied.

Author: Vasiliy Zdanovskiy
email: vasilyvz@gmail.com
"""
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Import mcp_security_framework components
from mcp_security_framework.core.cert_manager import CertificateManager
from mcp_security_framework.schemas.config import CAConfig, ServerCertConfig, ClientCertConfig, CertificateConfig
from mcp_security_framework.utils.cert_utils import validate_certificate_format

# Import required certificates configuration
from required_certificates import REQUIRED_CERTIFICATES, get_all_required_certificates


class BugfixCertificateGenerator:
    """Certificate generator using mcp_security_framework with bugfix."""
    
    def __init__(self):
        """Initialize the certificate generator."""
        self.working_dir = Path.cwd()
        self.certs_dir = self.working_dir / "certs"
        self.keys_dir = self.working_dir / "keys"
        
        # Ensure directories exist
        self.certs_dir.mkdir(exist_ok=True)
        self.keys_dir.mkdir(exist_ok=True)
        
        # Certificate manager will be initialized after CA is created
        self.cert_manager = None
    
    def print_step(self, step: str, description: str):
        """Print a formatted step header."""
        print(f"\n{'=' * 60}")
        print(f"🔧 STEP {step}: {description}")
        print(f"{'=' * 60}")
    
    def print_success(self, message: str):
        """Print a success message."""
        print(f"✅ {message}")
    
    def print_error(self, message: str):
        """Print an error message."""
        print(f"❌ {message}")
    
    def print_info(self, message: str):
        """Print an info message."""
        print(f"ℹ️  {message}")
    
    def check_framework(self) -> bool:
        """Check if mcp_security_framework is available."""
        try:
            from mcp_security_framework import __version__
            self.print_success(f"mcp_security_framework v{__version__} is available")
            return True
        except ImportError as e:
            self.print_error(f"mcp_security_framework is not available: {e}")
            return False
    
    def _initialize_cert_manager(self, ca_creation_mode: bool = False):
        """Initialize certificate manager with configuration."""
        cert_config = CertificateConfig(
            enabled=True,
            ca_creation_mode=ca_creation_mode,
            ca_cert_path=str(self.certs_dir / "ca_cert.pem") if not ca_creation_mode else None,
            ca_key_path=str(self.keys_dir / "ca_key.pem") if not ca_creation_mode else None,
            cert_storage_path=str(self.certs_dir),
            key_storage_path=str(self.keys_dir),
            default_validity_days=365,
            key_size=2048,
            hash_algorithm="sha256"
        )
        self.cert_manager = CertificateManager(cert_config)
    
    def generate_ca_certificate(self) -> bool:
        """Generate CA certificate using mcp_security_framework with bugfix."""
        self.print_step("1", "Generating CA Certificate with Bugfix")
        
        ca_info = REQUIRED_CERTIFICATES["ca_cert"]
        
        try:
            # Check if CA certificate already exists
            if ca_info["output_cert"].exists() and ca_info["output_key"].exists():
                self.print_info(f"CA certificate already exists: {ca_info['output_cert']}")
                return True
            
            # Create CA configuration
            ca_config = CAConfig(
                common_name=ca_info["common_name"],
                organization=ca_info["organization"],
                country=ca_info["country"],
                state=ca_info["state"],
                locality=ca_info["city"],
                validity_years=ca_info["validity_days"] // 365,
                key_size=2048,
                hash_algorithm="sha256"
            )
            
            self.print_info(f"Generating CA certificate: {ca_info['common_name']}")
            
            # Initialize certificate manager in CA creation mode
            self._initialize_cert_manager(ca_creation_mode=True)
            
            # Generate CA certificate using framework
            result = self.cert_manager.create_root_ca(ca_config=ca_config)
            
            if result:
                # Save the generated certificate and key to expected locations
                with open(ca_info["output_cert"], 'w') as f:
                    f.write(result.certificate_pem)
                with open(ca_info["output_key"], 'w') as f:
                    f.write(result.private_key_pem)
                
                self.print_success(f"CA certificate generated: {ca_info['output_cert']}")
                # Reinitialize certificate manager in normal mode
                self._initialize_cert_manager(ca_creation_mode=False)
                return True
            else:
                self.print_error("Failed to generate CA certificate")
                return False
                
        except Exception as e:
            self.print_error(f"Exception during CA certificate generation: {e}")
            return False
    
    def generate_server_certificate(self) -> bool:
        """Generate server certificate using mcp_security_framework."""
        self.print_step("2", "Generating Server Certificate")
        
        server_info = REQUIRED_CERTIFICATES["server_cert"]
        
        try:
            # Check if server certificate already exists
            if server_info["output_cert"].exists() and server_info["output_key"].exists():
                self.print_info(f"Server certificate already exists: {server_info['output_cert']}")
                return True
            
            # Ensure certificate manager is initialized in normal mode
            if self.cert_manager is None:
                self._initialize_cert_manager(ca_creation_mode=False)
            
            # Create server certificate configuration
            server_config = ServerCertConfig(
                common_name=server_info["common_name"],
                organization=server_info["organization"],
                country=server_info["country"],
                state=server_info["state"],
                locality=server_info["city"],
                validity_days=server_info["validity_days"],
                key_size=2048,
                hash_algorithm="sha256",
                ca_cert_path=str(server_info["ca_cert_path"]),
                ca_key_path=str(server_info["ca_key_path"]),
                san=server_info.get("san", [])
            )
            
            self.print_info(f"Generating server certificate: {server_info['common_name']}")
            
            # Generate server certificate using framework
            result = self.cert_manager.create_server_certificate(server_config=server_config)
            
            if result:
                # Save the generated certificate and key to expected locations
                with open(server_info["output_cert"], 'w') as f:
                    f.write(result.certificate_pem)
                with open(server_info["output_key"], 'w') as f:
                    f.write(result.private_key_pem)
                
                self.print_success(f"Server certificate generated: {server_info['output_cert']}")
                return True
            else:
                self.print_error("Failed to generate server certificate")
                return False
                
        except Exception as e:
            self.print_error(f"Exception during server certificate generation: {e}")
            return False
    
    def generate_client_certificate(self, cert_name: str) -> bool:
        """Generate client certificate using mcp_security_framework."""
        self.print_step(f"3.{cert_name}", f"Generating {cert_name.title()} Client Certificate")
        
        client_info = REQUIRED_CERTIFICATES[cert_name]
        
        try:
            # Check if client certificate already exists
            if client_info["output_cert"].exists() and client_info["output_key"].exists():
                self.print_info(f"{cert_name} certificate already exists: {client_info['output_cert']}")
                return True
            
            # Ensure certificate manager is initialized in normal mode
            if self.cert_manager is None:
                self._initialize_cert_manager(ca_creation_mode=False)
            
            # Create client certificate configuration
            client_config = ClientCertConfig(
                common_name=client_info["common_name"],
                organization=client_info["organization"],
                country=client_info["country"],
                state=client_info["state"],
                locality=client_info["city"],
                validity_days=client_info["validity_days"],
                key_size=2048,
                hash_algorithm="sha256",
                ca_cert_path=str(client_info["ca_cert_path"]),
                ca_key_path=str(client_info["ca_key_path"]),
                roles=client_info.get("roles", []),
                permissions=client_info.get("permissions", [])
            )
            
            self.print_info(f"Generating {cert_name} certificate: {client_info['common_name']}")
            
            # Generate client certificate using framework
            result = self.cert_manager.create_client_certificate(client_config=client_config)
            
            if result:
                # Save the generated certificate and key to expected locations
                with open(client_info["output_cert"], 'w') as f:
                    f.write(result.certificate_pem)
                with open(client_info["output_key"], 'w') as f:
                    f.write(result.private_key_pem)
                
                # Also create a copy in certs/ directory for easier access
                cert_name_base = client_info["common_name"].replace("-", "_")
                certs_cert = self.certs_dir / f"{cert_name_base}_client.crt"
                certs_key = self.certs_dir / f"{cert_name_base}_client.key"
                
                with open(certs_cert, 'w') as f:
                    f.write(result.certificate_pem)
                with open(certs_key, 'w') as f:
                    f.write(result.private_key_pem)
                
                self.print_success(f"{cert_name} certificate generated: {client_info['output_cert']}")
                self.print_success(f"Also created: {certs_cert} and {certs_key}")
                return True
            else:
                self.print_error(f"Failed to generate {cert_name} certificate")
                return False
                
        except Exception as e:
            self.print_error(f"Exception during {cert_name} certificate generation: {e}")
            return False
    
    def create_certificate_aliases(self) -> bool:
        """Create certificate aliases for different configurations."""
        self.print_step("4", "Creating Certificate Aliases")
        
        try:
            # Create aliases for HTTPS configurations
            if (self.certs_dir / "server_cert.pem").exists():
                # HTTPS aliases
                (self.certs_dir / "mcp_proxy_adapter_server.crt").unlink(missing_ok=True)
                (self.certs_dir / "mcp_proxy_adapter_server.crt").symlink_to("server_cert.pem")
                
                (self.certs_dir / "mcp_proxy_adapter_server.key").unlink(missing_ok=True)
                (self.certs_dir / "mcp_proxy_adapter_server.key").symlink_to(self.keys_dir / "server_key.pem")
                
                # mTLS aliases
                (self.certs_dir / "localhost_server.crt").unlink(missing_ok=True)
                (self.certs_dir / "localhost_server.crt").symlink_to("server_cert.pem")
                
                self.print_success("Certificate aliases created")
            
            # Create CA alias
            if (self.certs_dir / "ca_cert.pem").exists():
                (self.certs_dir / "mcp_proxy_adapter_ca_ca.crt").unlink(missing_ok=True)
                (self.certs_dir / "mcp_proxy_adapter_ca_ca.crt").symlink_to("ca_cert.pem")
                
                self.print_success("CA certificate alias created")
            
            return True
            
        except Exception as e:
            self.print_error(f"Failed to create certificate aliases: {e}")
            return False
    
    def validate_certificates(self) -> bool:
        """Validate generated certificates using framework."""
        self.print_step("5", "Validating Certificates")
        
        all_required = get_all_required_certificates()
        validation_results = []
        
        for cert_name in all_required:
            cert_info = REQUIRED_CERTIFICATES[cert_name]
            cert_file = cert_info["output_cert"]
            key_file = cert_info["output_key"]
            
            if cert_file.exists() and key_file.exists():
                try:
                    # Validate certificate format using framework
                    format_valid = validate_certificate_format(str(cert_file))
                    
                    if format_valid:
                        self.print_success(f"{cert_name}: Valid format")
                        validation_results.append(True)
                    else:
                        self.print_error(f"{cert_name}: Invalid format")
                        validation_results.append(False)
                        
                except Exception as e:
                    self.print_error(f"{cert_name}: Validation failed - {e}")
                    validation_results.append(False)
            else:
                self.print_error(f"{cert_name}: Missing files")
                validation_results.append(False)
        
        success_count = sum(validation_results)
        total_count = len(validation_results)
        
        self.print_info(f"Validation results: {success_count}/{total_count} certificates valid")
        
        return success_count == total_count
    
    def generate_all_certificates(self) -> bool:
        """Generate all required certificates."""
        print("🔐 Generating All Certificates Using mcp_security_framework with Bugfix")
        print("=" * 60)
        
        try:
            # Check framework availability
            if not self.check_framework():
                return False
            
            # Generate CA certificate first
            if not self.generate_ca_certificate():
                return False
            
            # Generate server certificate
            if not self.generate_server_certificate():
                return False
            
            # Generate client certificates
            client_certs = ["admin_cert", "user_cert", "proxy_cert"]
            for cert_name in client_certs:
                if cert_name in REQUIRED_CERTIFICATES:
                    if not self.generate_client_certificate(cert_name):
                        return False
            
            # Create aliases
            if not self.create_certificate_aliases():
                return False
            
            # Validate certificates
            if not self.validate_certificates():
                return False
            
            # Print summary
            print(f"\n{'=' * 60}")
            print("📊 CERTIFICATE GENERATION SUMMARY")
            print(f"{'=' * 60}")
            print("✅ All certificates generated successfully!")
            print(f"📁 Certificates directory: {self.certs_dir}")
            print(f"📁 Keys directory: {self.keys_dir}")
            
            return True
            
        except Exception as e:
            self.print_error(f"Certificate generation failed: {e}")
            return False


def main():
    """Main entry point."""
    generator = BugfixCertificateGenerator()
    
    try:
        success = generator.generate_all_certificates()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
