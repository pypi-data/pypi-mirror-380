#!/usr/bin/env python3
"""
MCP Proxy Adapter - Main Entry Point

Author: Vasiliy Zdanovskiy
email: vasilyvz@gmail.com
"""
import sys
import ssl
import hypercorn.asyncio
import hypercorn.config
import asyncio
import argparse
from pathlib import Path

# Add the project root to the path only if running from source
# This allows the installed package to be used when installed via pip
if not str(Path(__file__).parent.parent) in sys.path:
    sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp_proxy_adapter.api.app import create_app
from mcp_proxy_adapter.config import Config
from mcp_proxy_adapter.core.config_validator import ConfigValidator


def main():
    """Main entry point for the MCP Proxy Adapter."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="MCP Proxy Adapter Server",
    )
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        help="Path to configuration file",
    )
    args = parser.parse_args()

    # Load configuration
    if args.config:
        config = Config(config_path=args.config)
    else:
        config = Config()

    # Validate UUID configuration (mandatory)
    validator = ConfigValidator(config.get_all())
    if not validator.validate_all():
        print("❌ Configuration validation failed:")
        for error in validator.get_errors():
            print(f"   - {error}")
        sys.exit(1)
    print("✅ Configuration validation passed")

    # Create application (pass config_path so reload uses same file)
    app = create_app(app_config=config.get_all(), config_path=args.config)

    # Get server configuration
    host = config.get("server.host", "0.0.0.0")
    port = config.get("server.port", 8000)

    # Get protocol and SSL configuration
    protocol = config.get("server.protocol", "http")
    ssl_enabled = protocol in ["https", "mtls"]
    
    # SSL configuration based on protocol
    ssl_cert_file = None
    ssl_key_file = None
    ssl_ca_cert = None
    verify_client = False
    
    if ssl_enabled:
        # Configure SSL based on protocol
        if protocol == "https":
            # HTTPS - server SSL only
            ssl_cert_file = "../../certs/server.crt"
            ssl_key_file = "../../certs/server.key"
            ssl_ca_cert = "../../certs/localhost_server.crt"
            verify_client = False

        elif protocol == "mtls":
            # mTLS - server SSL + client certificate verification
            # Use server.crt and server.key for server, and localhost_server.crt as CA
            ssl_cert_file = "../../certs/server.crt"
            ssl_key_file = "../../certs/server.key"
            ssl_ca_cert = "../../certs/localhost_server.crt"
            verify_client = False  # Disable client cert verification for testing

    print("🔍 Debug config:")
    print(f"   protocol: {protocol}")
    print(f"   ssl_enabled: {ssl_enabled}")
    print("🔍 Source: configuration")

    print("🚀 Starting MCP Proxy Adapter")
    print(f"🌐 Server: {host}:{port}")
    print(f"🔒 Protocol: {protocol}")
    if ssl_enabled:
        print("🔐 SSL: Enabled")
        print(f"   Certificate: {ssl_cert_file}")
        print(f"   Key: {ssl_key_file}")
        if ssl_ca_cert:
            print(f"   CA: {ssl_ca_cert}")
        print(f"   Client verification: {verify_client}")
    print("=" * 50)

    # Configure hypercorn using framework
    config_hypercorn = hypercorn.config.Config()
    config_hypercorn.bind = [f"{host}:{port}"]

    if ssl_enabled and ssl_cert_file and ssl_key_file:
        # Use framework to convert SSL configuration
        from mcp_proxy_adapter.core.server_adapter import ServerConfigAdapter
        
        ssl_config = {
            "cert_file": ssl_cert_file,
            "key_file": ssl_key_file,
            "ca_cert": ssl_ca_cert,
            "verify_client": verify_client,
            "chk_hostname": config.get("transport.ssl.chk_hostname", True)
        }
        
        hypercorn_ssl = ServerConfigAdapter.convert_ssl_config_for_engine(ssl_config, "hypercorn")
        
        # Apply converted SSL configuration
        for key, value in hypercorn_ssl.items():
            setattr(config_hypercorn, key, value)
        
        print("🔐 SSL: Configured via framework")
        if verify_client:
            print("🔐 mTLS: Client certificate verification enabled")
        else:
            print("🔐 HTTPS: Regular HTTPS without client certificate verification")
        
        chk_hostname = ssl_config.get("chk_hostname", True)
        print(f"🔍 Hostname checking: {'enabled' if chk_hostname else 'disabled'}")

        # Prefer modern protocols
        try:
            config_hypercorn.alpn_protocols = ["h2", "http/1.1"]
        except Exception:
            pass

    # Log hypercorn configuration
    print("=" * 50)
    print("🔍 HYPERCORN CONFIGURATION:")
    print(
        "🔍 certfile="
        f"{getattr(config_hypercorn, 'certfile', None)}",
    )
    print(
        "🔍 keyfile="
        f"{getattr(config_hypercorn, 'keyfile', None)}",
    )
    print(
        "🔍 ca_certs="
        f"{getattr(config_hypercorn, 'ca_certs', None)}",
    )
    print(
        "🔍 verify_mode="
        f"{getattr(config_hypercorn, 'verify_mode', None)}",
    )
    print(
        "🔍 alpn_protocols="
        f"{getattr(config_hypercorn, 'alpn_protocols', None)}",
    )
    print("=" * 50)

    if ssl_enabled:
        print("🔐 Starting HTTPS server with hypercorn...")
    else:
        print("🌐 Starting HTTP server with hypercorn...")

    # Run the server
    asyncio.run(hypercorn.asyncio.serve(app, config_hypercorn))


if __name__ == "__main__":
    main()
