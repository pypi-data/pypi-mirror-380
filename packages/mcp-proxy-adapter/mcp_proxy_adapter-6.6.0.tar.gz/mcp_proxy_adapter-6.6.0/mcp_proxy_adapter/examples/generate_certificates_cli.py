#!/usr/bin/env python3
"""
Generate Certificates Using mcp_security_framework CLI
This script generates all necessary SSL certificates using the mcp_security_framework CLI.

Author: Vasiliy Zdanovskiy
email: vasilyvz@gmail.com
"""
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Import required certificates configuration
from required_certificates import REQUIRED_CERTIFICATES, get_all_required_certificates


class CLICertificateGenerator:
    """Certificate generator using mcp_security_framework CLI."""
    
    def __init__(self):
        """Initialize the certificate generator."""
        self.working_dir = Path.cwd()
        self.certs_dir = self.working_dir / "certs"
        self.keys_dir = self.working_dir / "keys"
        
        # Ensure directories exist
        self.certs_dir.mkdir(exist_ok=True)
        self.keys_dir.mkdir(exist_ok=True)
    
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
        """Check if mcp_security_framework CLI is available."""
        try:
            result = subprocess.run([
                sys.executable, "-m", "mcp_security_framework.cli.cert_cli", "--help"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                self.print_success("mcp_security_framework CLI is available")
                return True
            else:
                self.print_error("mcp_security_framework CLI is not available")
                return False
        except Exception as e:
            self.print_error(f"Failed to check framework: {e}")
            return False
    
    def create_ca_certificate_manually(self) -> bool:
        """Create CA certificate manually using OpenSSL."""
        self.print_step("1", "Creating CA Certificate Manually")
        
        ca_info = REQUIRED_CERTIFICATES["ca_cert"]
        
        try:
            # Check if CA certificate already exists
            if ca_info["output_cert"].exists() and ca_info["output_key"].exists():
                self.print_info(f"CA certificate already exists: {ca_info['output_cert']}")
                return True
            
            # Generate CA private key
            key_cmd = [
                "openssl", "genrsa", "-out", str(ca_info["output_key"]), "2048"
            ]
            
            self.print_info("Generating CA private key...")
            result = subprocess.run(key_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode != 0:
                self.print_error(f"Failed to generate CA key: {result.stderr}")
                return False
            
            # Generate CA certificate
            cert_cmd = [
                "openssl", "req", "-new", "-x509", "-days", str(ca_info["validity_days"]),
                "-key", str(ca_info["output_key"]), "-out", str(ca_info["output_cert"]),
                "-subj", f"/C={ca_info['country']}/ST={ca_info['state']}/L={ca_info['city']}/O={ca_info['organization']}/CN={ca_info['common_name']}"
            ]
            
            self.print_info(f"Creating CA certificate: {ca_info['common_name']}")
            result = subprocess.run(cert_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode == 0:
                self.print_success(f"CA certificate created: {ca_info['output_cert']}")
                return True
            else:
                self.print_error(f"Failed to create CA certificate: {result.stderr}")
                return False
                
        except Exception as e:
            self.print_error(f"Exception during CA certificate creation: {e}")
            return False
    
    def generate_server_certificate_with_framework(self) -> bool:
        """Generate server certificate using mcp_security_framework CLI."""
        self.print_step("2", "Generating Server Certificate with Framework")
        
        server_info = REQUIRED_CERTIFICATES["server_cert"]
        
        try:
            # Check if server certificate already exists
            if server_info["output_cert"].exists() and server_info["output_key"].exists():
                self.print_info(f"Server certificate already exists: {server_info['output_cert']}")
                return True
            
            # Create configuration file for framework
            config_file = self.working_dir / "cert_config.json"
            config = {
                "ca": {
                    "cert_path": str(server_info["ca_cert_path"]),
                    "key_path": str(server_info["ca_key_path"])
                },
                "certificates": {
                    "storage_path": str(self.certs_dir),
                    "key_storage_path": str(self.keys_dir),
                    "default_validity_days": server_info["validity_days"],
                    "key_size": 2048,
                    "hash_algorithm": "sha256"
                }
            }
            
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            # Generate server certificate using framework CLI
            cmd = [
                sys.executable, "-m", "mcp_security_framework.cli.cert_cli",
                "-c", str(config_file),
                "create-server",
                "-cn", server_info["common_name"],
                "-o", server_info["organization"],
                "-c", server_info["country"],
                "-s", server_info["state"],
                "-l", server_info["city"],
                "-d", str(server_info["validity_days"])
            ]
            
            # Add SAN if specified
            if "san" in server_info:
                for san in server_info["san"]:
                    cmd.extend(["--san", san])
            
            self.print_info(f"Generating server certificate: {server_info['common_name']}")
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode == 0:
                # Move generated files to expected locations
                generated_cert = self.certs_dir / f"{server_info['common_name']}.crt"
                generated_key = self.keys_dir / f"{server_info['common_name']}.key"
                
                if generated_cert.exists():
                    generated_cert.rename(server_info["output_cert"])
                if generated_key.exists():
                    generated_key.rename(server_info["output_key"])
                
                self.print_success(f"Server certificate generated: {server_info['output_cert']}")
                return True
            else:
                self.print_error(f"Failed to generate server certificate: {result.stderr}")
                return False
                
        except Exception as e:
            self.print_error(f"Exception during server certificate generation: {e}")
            return False
        finally:
            # Clean up config file
            if config_file.exists():
                config_file.unlink()
    
    def generate_client_certificate_with_framework(self, cert_name: str) -> bool:
        """Generate client certificate using mcp_security_framework CLI."""
        self.print_step(f"3.{cert_name}", f"Generating {cert_name.title()} Client Certificate with Framework")
        
        client_info = REQUIRED_CERTIFICATES[cert_name]
        
        try:
            # Check if client certificate already exists
            if client_info["output_cert"].exists() and client_info["output_key"].exists():
                self.print_info(f"{cert_name} certificate already exists: {client_info['output_cert']}")
                return True
            
            # Create configuration file for framework
            config_file = self.working_dir / "cert_config.json"
            config = {
                "ca": {
                    "cert_path": str(client_info["ca_cert_path"]),
                    "key_path": str(client_info["ca_key_path"])
                },
                "certificates": {
                    "storage_path": str(self.certs_dir),
                    "key_storage_path": str(self.keys_dir),
                    "default_validity_days": client_info["validity_days"],
                    "key_size": 2048,
                    "hash_algorithm": "sha256"
                }
            }
            
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            # Generate client certificate using framework CLI
            cmd = [
                sys.executable, "-m", "mcp_security_framework.cli.cert_cli",
                "-c", str(config_file),
                "create-client",
                "-cn", client_info["common_name"],
                "-o", client_info["organization"],
                "-c", client_info["country"],
                "-s", client_info["state"],
                "-l", client_info["city"],
                "-d", str(client_info["validity_days"])
            ]
            
            # Add roles if specified
            if "roles" in client_info:
                for role in client_info["roles"]:
                    cmd.extend(["--roles", role])
            
            # Add permissions if specified
            if "permissions" in client_info:
                for permission in client_info["permissions"]:
                    cmd.extend(["--permissions", permission])
            
            self.print_info(f"Generating {cert_name} certificate: {client_info['common_name']}")
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode == 0:
                # Move generated files to expected locations
                generated_cert = self.certs_dir / f"{client_info['common_name']}.crt"
                generated_key = self.keys_dir / f"{client_info['common_name']}.key"
                
                if generated_cert.exists():
                    generated_cert.rename(client_info["output_cert"])
                if generated_key.exists():
                    generated_key.rename(client_info["output_key"])
                
                self.print_success(f"{cert_name} certificate generated: {client_info['output_cert']}")
                return True
            else:
                self.print_error(f"Failed to generate {cert_name} certificate: {result.stderr}")
                return False
                
        except Exception as e:
            self.print_error(f"Exception during {cert_name} certificate generation: {e}")
            return False
        finally:
            # Clean up config file
            if config_file.exists():
                config_file.unlink()
    
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
    
    def validate_certificates_with_framework(self) -> bool:
        """Validate generated certificates using framework."""
        self.print_step("5", "Validating Certificates with Framework")
        
        all_required = get_all_required_certificates()
        validation_results = []
        
        for cert_name in all_required:
            cert_info = REQUIRED_CERTIFICATES[cert_name]
            cert_file = cert_info["output_cert"]
            
            if cert_file.exists():
                try:
                    # Validate certificate using framework CLI
                    cmd = [
                        sys.executable, "-m", "mcp_security_framework.cli.cert_cli",
                        "validate", str(cert_file)
                    ]
                    
                    result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.working_dir)
                    
                    if result.returncode == 0:
                        self.print_success(f"{cert_name}: Valid")
                        validation_results.append(True)
                    else:
                        self.print_error(f"{cert_name}: Invalid - {result.stderr}")
                        validation_results.append(False)
                        
                except Exception as e:
                    self.print_error(f"{cert_name}: Validation failed - {e}")
                    validation_results.append(False)
            else:
                self.print_error(f"{cert_name}: Missing certificate file")
                validation_results.append(False)
        
        success_count = sum(validation_results)
        total_count = len(validation_results)
        
        self.print_info(f"Validation results: {success_count}/{total_count} certificates valid")
        
        return success_count == total_count
    
    def generate_all_certificates(self) -> bool:
        """Generate all required certificates."""
        print("🔐 Generating All Certificates Using mcp_security_framework CLI")
        print("=" * 60)
        
        try:
            # Check framework availability
            if not self.check_framework():
                return False
            
            # Create CA certificate manually first
            if not self.create_ca_certificate_manually():
                return False
            
            # Generate server certificate with framework
            if not self.generate_server_certificate_with_framework():
                return False
            
            # Generate client certificates with framework
            client_certs = ["admin_cert", "user_cert", "proxy_cert"]
            for cert_name in client_certs:
                if cert_name in REQUIRED_CERTIFICATES:
                    if not self.generate_client_certificate_with_framework(cert_name):
                        return False
            
            # Create aliases
            if not self.create_certificate_aliases():
                return False
            
            # Validate certificates with framework
            if not self.validate_certificates_with_framework():
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
    generator = CLICertificateGenerator()
    
    try:
        success = generator.generate_all_certificates()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
