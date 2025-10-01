"""Encryptor package for ShadowSeal - Advanced Multi-Layer Encryption."""

from .encrypt import encrypt_file, _internal_decrypt_file

__all__ = ['encrypt_file']  # decrypt_file removed - irreversible encryption

# Internal use only - not exposed to public API
# _internal_decrypt_file available for debugging/development