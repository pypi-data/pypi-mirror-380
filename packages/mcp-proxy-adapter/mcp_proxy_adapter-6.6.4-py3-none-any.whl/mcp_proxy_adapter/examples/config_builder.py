#!/usr/bin/env python3
"""
Simplified Configuration Builder for MCP Proxy Adapter

Author: Vasiliy Zdanovskiy
email: vasilyvz@gmail.com
"""

import json
import uuid
from enum import Enum
from typing import Dict, List, Optional, Any


class Protocol(Enum):
    """Supported protocols."""
    HTTP = "http"
    HTTPS = "https"
    MTLS = "mtls"


class AuthMethod(Enum):
    """Authentication methods."""
    NONE = "none"
    TOKEN = "token"
    TOKEN_ROLES = "token_roles"


class ConfigBuilder:
    """Simplified configuration builder."""
    
    def __init__(self):
        """Initialize the configuration builder."""
        self._reset_to_defaults()
    
    def _reset_to_defaults(self):
        """Reset configuration to default values."""
        self.config = {
            "uuid": str(uuid.uuid4()),
            "server": {
                "host": "0.0.0.0",
                "port": 8000,
                "protocol": "http",
                "debug": False,
                "log_level": "INFO"
            },
            "logging": {
                "level": "INFO",
                "file": None,
                "log_dir": "./logs",
                "log_file": "mcp_proxy_adapter.log",
                "max_size": 10,
                "backup_count": 5,
                "console_output": True,
                "json_format": False
            },
            "security": {
                "enabled": False,
                "tokens": {
                    "admin": "admin-secret-key",
                    "user": "user-secret-key",
                    "readonly": "readonly-secret-key"
                },
                "roles": {
                    "admin": ["read", "write", "delete", "admin"],
                    "user": ["read", "write"],
                    "readonly": ["read"]
                },
                "roles_file": None
            },
            "debug": {
                "enabled": False,
                "log_level": "DEBUG",
                "trace_requests": False,
                "trace_responses": False
            },
            "transport": {
                "type": "http",
                        "port": None,
                "verify_client": False,
                "chk_hostname": False
            }
        }
    
    def set_protocol(self, protocol: Protocol, cert_dir: str = "./certs", key_dir: str = "./keys"):
        """Set protocol configuration (HTTP, HTTPS, or mTLS)."""
        self.config["server"]["protocol"] = protocol.value
        
        if protocol == Protocol.HTTP:
            # HTTP - no SSL, no client verification
            self.config["transport"]["verify_client"] = False
            self.config["transport"]["chk_hostname"] = False
            
        elif protocol == Protocol.HTTPS:
            # HTTPS - SSL enabled, no client verification
            self.config["transport"]["verify_client"] = False
            self.config["transport"]["chk_hostname"] = True
            
        elif protocol == Protocol.MTLS:
            # mTLS - SSL enabled, client verification required
            self.config["transport"]["verify_client"] = True
            self.config["transport"]["chk_hostname"] = True
        
        return self
    
    def set_auth(self, auth_method: AuthMethod, api_keys: Optional[Dict[str, str]] = None, roles: Optional[Dict[str, List[str]]] = None):
        """Set authentication configuration."""
        if auth_method == AuthMethod.NONE:
            self.config["security"]["enabled"] = False
            self.config["security"]["tokens"] = {}
            self.config["security"]["roles"] = {}
            self.config["security"]["roles_file"] = None
            
        elif auth_method == AuthMethod.TOKEN:
            self.config["security"]["enabled"] = True
            self.config["security"]["tokens"] = api_keys or {
                "admin": "admin-secret-key",
                "user": "user-secret-key"
            }
            self.config["security"]["roles"] = roles or {
                "admin": ["read", "write", "delete", "admin"],
                "user": ["read", "write"]
            }
            self.config["security"]["roles_file"] = None
            
        elif auth_method == AuthMethod.TOKEN_ROLES:
            self.config["security"]["enabled"] = True
            self.config["security"]["tokens"] = api_keys or {
                "admin": "admin-secret-key",
                "user": "user-secret-key",
                "readonly": "readonly-secret-key"
            }
            self.config["security"]["roles"] = roles or {
                "admin": ["read", "write", "delete", "admin"],
                "user": ["read", "write"],
                "readonly": ["read"]
            }
            self.config["security"]["roles_file"] = "configs/roles.json"
        
        return self
    
    def set_server(self, host: str = "0.0.0.0", port: int = 8000):
        """Set server configuration."""
        self.config["server"]["host"] = host
        self.config["server"]["port"] = port
        return self
    
    def set_roles_file(self, roles_file: str):
        """Set roles file path."""
        self.config["security"]["roles_file"] = roles_file
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build and return the configuration."""
        return self.config.copy()
    
    def save(self, file_path: str) -> None:
        """Save configuration to file."""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)


class ConfigFactory:
    """Factory for creating common configurations."""
    
    @staticmethod
    def create_http_config(port: int = 8000) -> Dict[str, Any]:
        """Create HTTP configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTP)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_http_token_config(port: int = 8001) -> Dict[str, Any]:
        """Create HTTP with token authentication configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTP)
                .set_auth(AuthMethod.TOKEN)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_http_token_roles_config(port: int = 8002) -> Dict[str, Any]:
        """Create HTTP with token and roles configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTP)
                .set_auth(AuthMethod.TOKEN_ROLES)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_https_config(port: int = 8003) -> Dict[str, Any]:
        """Create HTTPS configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTPS)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_https_token_config(port: int = 8004) -> Dict[str, Any]:
        """Create HTTPS with token authentication configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTPS)
                .set_auth(AuthMethod.TOKEN)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_https_token_roles_config(port: int = 8005) -> Dict[str, Any]:
        """Create HTTPS with token and roles configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTPS)
                .set_auth(AuthMethod.TOKEN_ROLES)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_mtls_config(port: int = 8006) -> Dict[str, Any]:
        """Create mTLS configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.MTLS)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_mtls_token_config(port: int = 8007) -> Dict[str, Any]:
        """Create mTLS with token authentication configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.MTLS)
                .set_auth(AuthMethod.TOKEN)
                .set_server(port=port)
                .build())

    @staticmethod
    def create_mtls_token_roles_config(port: int = 8008) -> Dict[str, Any]:
        """Create mTLS with token and roles configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.MTLS)
                .set_auth(AuthMethod.TOKEN_ROLES)
                .set_server(port=port)
                .build())


def create_config_from_flags(protocol: str, token: bool = False, roles: bool = False, port: int = 8000) -> Dict[str, Any]:
    """
    Create configuration from command line flags.
    
    Args:
        protocol: Protocol type (http, https, mtls)
        token: Enable token authentication
        roles: Enable role-based access control
        port: Server port
        
    Returns:
        Configuration dictionary
    """
    protocol_map = {
        "http": Protocol.HTTP,
        "https": Protocol.HTTPS,
        "mtls": Protocol.MTLS
    }
    
    if protocol not in protocol_map:
        raise ValueError(f"Unsupported protocol: {protocol}")
    
    builder = ConfigBuilder().set_protocol(protocol_map[protocol]).set_server(port=port)
    
    if roles:
        builder.set_auth(AuthMethod.TOKEN_ROLES)
    elif token:
        builder.set_auth(AuthMethod.TOKEN)
    else:
        builder.set_auth(AuthMethod.NONE)
    
    return builder.build()


if __name__ == "__main__":
    # Example usage
    config = create_config_from_flags("http", token=True, port=8001)
    print(json.dumps(config, indent=2))
