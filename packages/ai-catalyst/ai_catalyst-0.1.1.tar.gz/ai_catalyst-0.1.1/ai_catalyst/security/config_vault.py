"""
Secure Configuration Manager with encryption support
"""

import os
import json
import base64
from typing import Any, Dict, Optional
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import logging

logger = logging.getLogger(__name__)


class SecureConfigManager:
    """Secure configuration manager with encryption for sensitive values"""
    
    def __init__(self, master_key: Optional[str] = None, salt: Optional[bytes] = None):
        """
        Initialize secure config manager
        
        Args:
            master_key: Master encryption key (uses env var if not provided)
            salt: Salt for key derivation (generates if not provided)
        """
        self.master_key = master_key or os.getenv('AI_CATALYST_MASTER_KEY')
        self.salt = salt or os.urandom(16)
        self._cipher = None
        self._encrypted_keys = set()
        
        if self.master_key:
            self._initialize_cipher()
    
    def _initialize_cipher(self):
        """Initialize encryption cipher"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_key.encode()))
        self._cipher = Fernet(key)
    
    def encrypt_value(self, value: str) -> str:
        """Encrypt a configuration value"""
        if not self._cipher:
            raise ValueError("No master key configured for encryption")
        
        encrypted = self._cipher.encrypt(value.encode())
        return base64.urlsafe_b64encode(encrypted).decode()
    
    def decrypt_value(self, encrypted_value: str) -> str:
        """Decrypt a configuration value"""
        if not self._cipher:
            raise ValueError("No master key configured for decryption")
        
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_value.encode())
            decrypted = self._cipher.decrypt(encrypted_bytes)
            return decrypted.decode()
        except Exception as e:
            raise ValueError(f"Failed to decrypt value: {e}")
    
    def set_secure(self, key: str, value: str, encrypt: bool = True) -> Dict[str, Any]:
        """
        Set a secure configuration value
        
        Args:
            key: Configuration key
            value: Configuration value
            encrypt: Whether to encrypt the value
            
        Returns:
            Dict with encrypted value and metadata
        """
        if encrypt and self._cipher:
            encrypted_value = self.encrypt_value(value)
            self._encrypted_keys.add(key)
            return {
                'value': encrypted_value,
                'encrypted': True,
                'salt': base64.urlsafe_b64encode(self.salt).decode()
            }
        else:
            return {
                'value': value,
                'encrypted': False
            }
    
    def get_secure(self, config_data: Dict[str, Any]) -> str:
        """
        Get a secure configuration value
        
        Args:
            config_data: Configuration data dict
            
        Returns:
            Decrypted value
        """
        if config_data.get('encrypted', False):
            return self.decrypt_value(config_data['value'])
        else:
            return config_data['value']
    
    def is_encrypted(self, key: str) -> bool:
        """Check if a key is marked as encrypted"""
        return key in self._encrypted_keys
    
    def rotate_key(self, new_master_key: str, config_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Rotate encryption key and re-encrypt all encrypted values
        
        Args:
            new_master_key: New master key
            config_dict: Configuration dictionary to re-encrypt
            
        Returns:
            Re-encrypted configuration dictionary
        """
        if not self._cipher:
            raise ValueError("No current cipher for key rotation")
        
        # Decrypt all values with old key
        decrypted_values = {}
        for key, value in config_dict.items():
            if isinstance(value, dict) and value.get('encrypted', False):
                decrypted_values[key] = self.decrypt_value(value['value'])
        
        # Initialize new cipher
        old_master_key = self.master_key
        self.master_key = new_master_key
        self.salt = os.urandom(16)  # New salt
        self._initialize_cipher()
        
        # Re-encrypt with new key
        new_config = config_dict.copy()
        for key, decrypted_value in decrypted_values.items():
            new_config[key] = self.set_secure(key, decrypted_value, encrypt=True)
        
        logger.info(f"Rotated encryption key for {len(decrypted_values)} encrypted values")
        return new_config
    
    def export_encrypted_config(self, config_dict: Dict[str, Any]) -> str:
        """Export configuration as encrypted JSON string"""
        return json.dumps({
            'config': config_dict,
            'salt': base64.urlsafe_b64encode(self.salt).decode(),
            'encrypted_keys': list(self._encrypted_keys)
        })
    
    def import_encrypted_config(self, encrypted_json: str) -> Dict[str, Any]:
        """Import configuration from encrypted JSON string"""
        data = json.loads(encrypted_json)
        
        # Restore salt and encrypted keys
        self.salt = base64.urlsafe_b64decode(data['salt'].encode())
        self._encrypted_keys = set(data['encrypted_keys'])
        
        # Re-initialize cipher with restored salt
        if self.master_key:
            self._initialize_cipher()
        
        return data['config']
    
    @classmethod
    def generate_master_key(cls) -> str:
        """Generate a new master key"""
        return base64.urlsafe_b64encode(os.urandom(32)).decode()