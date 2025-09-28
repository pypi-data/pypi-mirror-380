#!/usr/bin/env python3
"""
Generate Certificates Using OpenSSL
This script generates all necessary SSL certificates using OpenSSL directly.

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


class OpenSSLCertificateGenerator:
    """Certificate generator using OpenSSL directly."""
    
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
    
    def check_openssl(self) -> bool:
        """Check if OpenSSL is available."""
        try:
            result = subprocess.run(["openssl", "version"], capture_output=True, text=True)
            if result.returncode == 0:
                self.print_success(f"OpenSSL is available: {result.stdout.strip()}")
                return True
            else:
                self.print_error("OpenSSL is not available")
                return False
        except FileNotFoundError:
            self.print_error("OpenSSL is not installed")
            return False
    
    def generate_ca_certificate(self) -> bool:
        """Generate CA certificate using OpenSSL."""
        self.print_step("1", "Generating CA Certificate")
        
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
            
            self.print_info(f"Generating CA certificate: {ca_info['common_name']}")
            result = subprocess.run(cert_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode == 0:
                self.print_success(f"CA certificate generated: {ca_info['output_cert']}")
                return True
            else:
                self.print_error(f"Failed to generate CA certificate: {result.stderr}")
                return False
                
        except Exception as e:
            self.print_error(f"Exception during CA certificate generation: {e}")
            return False
    
    def generate_server_certificate(self) -> bool:
        """Generate server certificate using OpenSSL."""
        self.print_step("2", "Generating Server Certificate")
        
        server_info = REQUIRED_CERTIFICATES["server_cert"]
        
        try:
            # Check if server certificate already exists
            if server_info["output_cert"].exists() and server_info["output_key"].exists():
                self.print_info(f"Server certificate already exists: {server_info['output_cert']}")
                return True
            
            # Generate server private key
            key_cmd = [
                "openssl", "genrsa", "-out", str(server_info["output_key"]), "2048"
            ]
            
            self.print_info("Generating server private key...")
            result = subprocess.run(key_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode != 0:
                self.print_error(f"Failed to generate server key: {result.stderr}")
                return False
            
            # Create certificate signing request
            csr_file = self.certs_dir / "server.csr"
            csr_cmd = [
                "openssl", "req", "-new", "-key", str(server_info["output_key"]),
                "-out", str(csr_file),
                "-subj", f"/C={server_info['country']}/ST={server_info['state']}/L={server_info['city']}/O={server_info['organization']}/CN={server_info['common_name']}"
            ]
            
            self.print_info("Creating certificate signing request...")
            result = subprocess.run(csr_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode != 0:
                self.print_error(f"Failed to create CSR: {result.stderr}")
                return False
            
            # Create extensions file for SAN
            ext_file = self.certs_dir / "server.ext"
            with open(ext_file, 'w') as f:
                f.write("authorityKeyIdentifier=keyid,issuer\n")
                f.write("basicConstraints=CA:FALSE\n")
                f.write("keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment\n")
                if "san" in server_info:
                    f.write("subjectAltName = @alt_names\n")
                    f.write("[alt_names]\n")
                    for i, san in enumerate(server_info["san"], 1):
                        if san.startswith("127.") or san.startswith("192.") or san.startswith("10."):
                            f.write(f"IP.{i} = {san}\n")
                        else:
                            f.write(f"DNS.{i} = {san}\n")
            
            # Sign the certificate with CA
            cert_cmd = [
                "openssl", "x509", "-req", "-in", str(csr_file),
                "-CA", str(server_info["ca_cert_path"]), "-CAkey", str(server_info["ca_key_path"]),
                "-CAcreateserial", "-out", str(server_info["output_cert"]),
                "-days", str(server_info["validity_days"]), "-extensions", "v3_req", "-extfile", str(ext_file)
            ]
            
            self.print_info(f"Generating server certificate: {server_info['common_name']}")
            result = subprocess.run(cert_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode == 0:
                self.print_success(f"Server certificate generated: {server_info['output_cert']}")
                # Clean up temporary files
                csr_file.unlink(missing_ok=True)
                ext_file.unlink(missing_ok=True)
                return True
            else:
                self.print_error(f"Failed to generate server certificate: {result.stderr}")
                return False
                
        except Exception as e:
            self.print_error(f"Exception during server certificate generation: {e}")
            return False
    
    def generate_client_certificate(self, cert_name: str) -> bool:
        """Generate client certificate using OpenSSL."""
        self.print_step(f"3.{cert_name}", f"Generating {cert_name.title()} Client Certificate")
        
        client_info = REQUIRED_CERTIFICATES[cert_name]
        
        try:
            # Check if client certificate already exists
            if client_info["output_cert"].exists() and client_info["output_key"].exists():
                self.print_info(f"{cert_name} certificate already exists: {client_info['output_cert']}")
                return True
            
            # Generate client private key
            key_cmd = [
                "openssl", "genrsa", "-out", str(client_info["output_key"]), "2048"
            ]
            
            self.print_info(f"Generating {cert_name} private key...")
            result = subprocess.run(key_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode != 0:
                self.print_error(f"Failed to generate {cert_name} key: {result.stderr}")
                return False
            
            # Create certificate signing request
            csr_file = self.certs_dir / f"{cert_name}.csr"
            csr_cmd = [
                "openssl", "req", "-new", "-key", str(client_info["output_key"]),
                "-out", str(csr_file),
                "-subj", f"/C={client_info['country']}/ST={client_info['state']}/L={client_info['city']}/O={client_info['organization']}/CN={client_info['common_name']}"
            ]
            
            self.print_info(f"Creating {cert_name} certificate signing request...")
            result = subprocess.run(csr_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode != 0:
                self.print_error(f"Failed to create {cert_name} CSR: {result.stderr}")
                return False
            
            # Sign the certificate with CA
            cert_cmd = [
                "openssl", "x509", "-req", "-in", str(csr_file),
                "-CA", str(client_info["ca_cert_path"]), "-CAkey", str(client_info["ca_key_path"]),
                "-CAcreateserial", "-out", str(client_info["output_cert"]),
                "-days", str(client_info["validity_days"])
            ]
            
            self.print_info(f"Generating {cert_name} certificate: {client_info['common_name']}")
            result = subprocess.run(cert_cmd, capture_output=True, text=True, cwd=self.working_dir)
            
            if result.returncode == 0:
                self.print_success(f"{cert_name} certificate generated: {client_info['output_cert']}")
                # Clean up temporary files
                csr_file.unlink(missing_ok=True)
                return True
            else:
                self.print_error(f"Failed to generate {cert_name} certificate: {result.stderr}")
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
        """Validate generated certificates."""
        self.print_step("5", "Validating Certificates")
        
        all_required = get_all_required_certificates()
        validation_results = []
        
        for cert_name in all_required:
            cert_info = REQUIRED_CERTIFICATES[cert_name]
            cert_file = cert_info["output_cert"]
            key_file = cert_info["output_key"]
            
            if cert_file.exists() and key_file.exists():
                # Validate certificate and key match
                validate_cmd = [
                    "openssl", "x509", "-noout", "-modulus", "-in", str(cert_file)
                ]
                cert_result = subprocess.run(validate_cmd, capture_output=True, text=True)
                
                key_cmd = [
                    "openssl", "rsa", "-noout", "-modulus", "-in", str(key_file)
                ]
                key_result = subprocess.run(key_cmd, capture_output=True, text=True)
                
                if cert_result.returncode == 0 and key_result.returncode == 0:
                    if cert_result.stdout == key_result.stdout:
                        self.print_success(f"{cert_name}: Valid (certificate and key match)")
                        validation_results.append(True)
                    else:
                        self.print_error(f"{cert_name}: Certificate and key do not match")
                        validation_results.append(False)
                else:
                    self.print_error(f"{cert_name}: Invalid certificate or key")
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
        print("🔐 Generating All Certificates Using OpenSSL")
        print("=" * 60)
        
        try:
            # Check OpenSSL availability
            if not self.check_openssl():
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
    generator = OpenSSLCertificateGenerator()
    
    try:
        success = generator.generate_all_certificates()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
