import os
import sys
import time
import struct
import hashlib
import base64
import secrets
import zlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from utils.cross_platform import CrossPlatformManager

VERSION = 4  # Updated version for advanced multi-layer encryption
BLOCK_SIZE = 16
AES_KEY_SIZE = 32  # 256-bit AES
CHACHA_KEY_SIZE = 32  # 256-bit ChaCha20
PBKDF2_ITERATIONS = 600000  # Increased from 100,000 for stronger security
NONCE_SIZE = 12  # Standard nonce size for AESGCM and ChaCha20Poly1305

def generate_key_from_password(password: bytes, salt: bytes, length: int = 32) -> bytes:
    """Generate a secure key from password using PBKDF2 with 600,000 iterations"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),  # Upgraded to SHA512 for stronger hashing
        length=length,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password)

def generate_fixed_key() -> bytes:
    """Generate a deterministic key for passwordless encryption using hardware binding"""
    # Use hardware-specific information to generate a unique key
    platform_manager = CrossPlatformManager()
    platform_id = platform_manager.generate_cross_platform_id()
    
    # Generate a deterministic 32-byte key from platform ID
    key_material = hashlib.sha256(platform_id.encode()).digest()
    return key_material

def encrypt_data(data: bytes, key: bytes) -> bytes:
    """
    Multi-layer encryption using ChaCha20-Poly1305 + AES-256-GCM
    
    This provides defense-in-depth: even if one cipher is broken, 
    the data remains protected by the other layer.
    """
    # Compress data first to reduce size and add entropy
    compressed = zlib.compress(data, level=9)
    
    # Derive two separate keys from the master key
    key_material = hashlib.sha512(key).digest()
    chacha_key = key_material[:32]
    aes_key = key_material[32:]
    
    # Layer 1: ChaCha20-Poly1305 encryption
    chacha_cipher = ChaCha20Poly1305(chacha_key)
    nonce1 = secrets.token_bytes(NONCE_SIZE)
    layer1_encrypted = chacha_cipher.encrypt(nonce1, compressed, None)
    
    # Layer 2: AES-256-GCM encryption
    aes_cipher = AESGCM(aes_key)
    nonce2 = secrets.token_bytes(NONCE_SIZE)
    layer2_encrypted = aes_cipher.encrypt(nonce2, layer1_encrypted, None)
    
    # Combine nonces with encrypted data
    # Format: nonce1 (12 bytes) + nonce2 (12 bytes) + encrypted data
    return nonce1 + nonce2 + layer2_encrypted

def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
    """
    Multi-layer decryption using AES-256-GCM + ChaCha20-Poly1305
    Internal use only - not exposed to end users
    """
    if len(encrypted_data) < NONCE_SIZE * 2:
        raise ValueError("Invalid encrypted data format")
    
    # Extract nonces
    nonce1 = encrypted_data[:NONCE_SIZE]
    nonce2 = encrypted_data[NONCE_SIZE:NONCE_SIZE * 2]
    ciphertext = encrypted_data[NONCE_SIZE * 2:]
    
    # Derive the same keys used for encryption
    key_material = hashlib.sha512(key).digest()
    chacha_key = key_material[:32]
    aes_key = key_material[32:]
    
    # Layer 2: AES-256-GCM decryption
    aes_cipher = AESGCM(aes_key)
    layer1_encrypted = aes_cipher.decrypt(nonce2, ciphertext, None)
    
    # Layer 1: ChaCha20-Poly1305 decryption
    chacha_cipher = ChaCha20Poly1305(chacha_key)
    compressed = chacha_cipher.decrypt(nonce1, layer1_encrypted, None)
    
    # Decompress
    return zlib.decompress(compressed)

def simple_checksum(data: bytes) -> int:
    """Calculate checksum for integrity verification"""
    return int.from_bytes(hashlib.sha256(data).digest()[:4], 'big')

def pack_shc(encrypted_data: bytes, salt: bytes, version: int = VERSION, has_password: bool = True) -> bytes:
    """Pack encrypted data with metadata for cross-platform compatibility"""
    checksum = simple_checksum(encrypted_data)
    timestamp = int(time.time())
    
    # Add platform compatibility flags
    platform_manager = CrossPlatformManager()
    platform_id = platform_manager.generate_cross_platform_id()
    platform_hash = hashlib.sha256(platform_id.encode()).digest()[:8]  # Increased to 8 bytes
    
    # Combine flags: password flag + platform compatibility flag + multi-layer encryption flag
    flags = (1 if has_password else 0) | (1 << 1) | (1 << 2)  # Bit 2 = multi-layer encryption
    
    # New header format with enhanced security
    # Format: checksum (4) + version (4) + timestamp (8) + flags (1) + platform_hash (8) + salt_length (2)
    salt_length = len(salt) if has_password else 0
    header = struct.pack('>I I Q B 8s H', checksum, version, timestamp, flags, platform_hash, salt_length)
    
    if has_password:
        return header + salt + encrypted_data
    else:
        return header + encrypted_data

def unpack_shc(packed_data: bytes):
    """Unpack encrypted data from .shc format with cross-platform support"""
    # Handle both old (v2, v3) and new (v4+) formats
    if len(packed_data) < 17:
        raise ValueError("Invalid file format")
    
    # Check if this is the newest format (v4+)
    if len(packed_data) >= 27:  # New format has 27-byte header
        try:
            header = packed_data[:27]
            checksum, version, timestamp, flags, platform_hash, salt_length = struct.unpack('>I I Q B 8s H', header)
            
            # Check version compatibility
            if version >= 4:
                # Newest format with multi-layer encryption
                has_password = bool(flags & 1)
                
                if has_password and salt_length > 0:
                    if len(packed_data) < 27 + salt_length:
                        raise ValueError("Invalid file format")
                    salt = packed_data[27:27 + salt_length]
                    encrypted_data = packed_data[27 + salt_length:]
                else:
                    salt = b''
                    encrypted_data = packed_data[27:]
                
                computed_checksum = simple_checksum(encrypted_data)
                if computed_checksum != checksum:
                    raise ValueError("Checksum mismatch. File corrupted or tampered.")
                
                return encrypted_data, salt, version, has_password
            
        except struct.error:
            pass
    
    # Try v3 format (21-byte header)
    if len(packed_data) >= 21:
        try:
            header = packed_data[:21]
            checksum, version, timestamp, flags, platform_hash = struct.unpack('>I I Q B 4s', header)
            
            if version >= 3:
                has_password = bool(flags & 1)
                
                if has_password:
                    if len(packed_data) < 29:  # 21 + 8 (salt)
                        raise ValueError("Invalid file format")
                    salt = packed_data[21:29]
                    encrypted_data = packed_data[29:]
                else:
                    salt = b''
                    encrypted_data = packed_data[21:]
                
                computed_checksum = simple_checksum(encrypted_data)
                if computed_checksum != checksum:
                    raise ValueError("Checksum mismatch. File corrupted or tampered.")
                
                return encrypted_data, salt, version, has_password
            
        except struct.error:
            pass
    
    # Fallback to old format (v2)
    header = packed_data[:17]
    checksum, version, timestamp, flags = struct.unpack('>I I Q B', packed_data[:17])
    has_password = bool(flags & 1)
    
    if has_password:
        if len(packed_data) < 25:
            raise ValueError("Invalid file format")
        salt = packed_data[17:25]
        encrypted_data = packed_data[25:]
    else:
        salt = b''
        encrypted_data = packed_data[17:]
    
    computed_checksum = simple_checksum(encrypted_data)
    if computed_checksum != checksum:
        raise ValueError("Checksum mismatch. File corrupted or tampered.")
    
    return encrypted_data, salt, version, has_password

def encrypt_file(input_path: str, output_path: str, password: str = None, obfuscate: bool = True):
    """
    Encrypt a Python file with advanced multi-layer encryption
    
    Uses ChaCha20-Poly1305 + AES-256-GCM for maximum security
    Optional password protection with PBKDF2-HMAC-SHA512 (600,000 iterations)
    Optional polymorphic obfuscation for additional security
    """
    if not input_path.endswith('.py'):
        raise ValueError("Input file must be a .py file")
    
    # Read the Python file
    with open(input_path, 'rb') as f:
        data = f.read()
    
    # Apply polymorphic obfuscation before encryption (if enabled)
    if obfuscate:
        try:
            from obfuscator.polymorphic_obfuscator import apply_polymorphic_obfuscation
            source_code = data.decode('utf-8')
            obfuscated_code = apply_polymorphic_obfuscation(source_code)
            data = obfuscated_code.encode('utf-8')
            print(f"✅ Applied polymorphic obfuscation")
        except Exception as e:
            # Obfuscation failed, use original data
            print(f"⚠️  Obfuscation failed, proceeding without it: {e}")
            # Ensure data is back to original
            pass  # data is already the original bytes
    
    # Encode data
    data = base64.b64encode(data)
    
    if password is None:
        # Passwordless mode - use hardware-bound key
        key = generate_fixed_key()
        salt = b''
        encrypted = encrypt_data(data, key)
        packed = pack_shc(encrypted, salt, has_password=False)
        print(f"🔐 Encrypted {input_path} -> {output_path} (hardware-bound)")
        print(f"✅ Multi-layer encryption: ChaCha20-Poly1305 + AES-256-GCM")
    else:
        # Password mode - use PBKDF2 with 600,000 iterations
        salt = secrets.token_bytes(16)  # Increased salt size to 16 bytes
        key = generate_key_from_password(password.encode(), salt, length=64)  # 64 bytes for dual keys
        encrypted = encrypt_data(data, key)
        packed = pack_shc(encrypted, salt, has_password=True)
        print(f"🔐 Encrypted {input_path} -> {output_path}")
        print(f"🔑 Password: {password}")
        print(f"✅ Multi-layer encryption: ChaCha20-Poly1305 + AES-256-GCM")
        print(f"✅ Key derivation: PBKDF2-HMAC-SHA512 ({PBKDF2_ITERATIONS:,} iterations)")
    
    # Write output
    with open(output_path, 'wb') as f:
        f.write(packed)
    
    return password

def _internal_decrypt_file(input_path: str, output_path: str, password: str = None):
    """
    Internal decryption function - NOT FOR PUBLIC USE
    This function is only used internally for debugging/testing
    """
    with open(input_path, 'rb') as f:
        packed_data = f.read()
    
    encrypted_data, salt, version, has_password = unpack_shc(packed_data)
    
    if has_password:
        if password is None:
            raise ValueError("Password required for encrypted file")
        # Determine key length based on version
        key_length = 64 if version >= 4 else 32
        key = generate_key_from_password(password.encode(), salt, length=key_length)
    else:
        # Passwordless mode - use hardware-bound key
        key = generate_fixed_key()
    
    decrypted = decrypt_data(encrypted_data, key)
    
    # Decode from base64
    data = base64.b64decode(decrypted)
    
    with open(output_path, 'wb') as f:
        f.write(data)
    
    print(f"⚠️  Internal decryption: {input_path} -> {output_path}")
    print(f"⚠️  This feature is for development only and should not be used in production")

def run_encrypted_file(filepath: str, password: str = None):
    """
    Run an encrypted .shc file directly
    Internal function - users should use 'shadowseal run' command
    """
    with open(filepath, 'rb') as f:
        packed_data = f.read()
    
    encrypted_data, salt, version, has_password = unpack_shc(packed_data)
    
    if has_password:
        if password is None:
            raise ValueError("Password required for encrypted file")
        # Determine key length based on version
        key_length = 64 if version >= 4 else 32
        key = generate_key_from_password(password.encode(), salt, length=key_length)
    else:
        # Passwordless mode - use hardware-bound key
        key = generate_fixed_key()
    
    decrypted = decrypt_data(encrypted_data, key)
    
    # Decode from base64
    data = base64.b64decode(decrypted)
    code_str = data.decode('utf-8')
    
    # Execute in restricted globals
    exec_globals = {
        '__builtins__': __builtins__,
        '__name__': '__main__',
        '__file__': filepath,
    }
    
    code_obj = compile(code_str, filepath, 'exec')
    exec(code_obj, exec_globals)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Advanced Python file encryption with multi-layer security')
    subparsers = parser.add_subparsers(dest='command')
    
    # Encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a Python file')
    encrypt_parser.add_argument('input', help='Input .py file')
    encrypt_parser.add_argument('-o', '--output', help='Output .shc file', required=True)
    encrypt_parser.add_argument('-p', '--password', help='Encryption password (optional - hardware-bound if not provided)')
    
    # Run command
    run_parser = subparsers.add_parser('run', help='Run an encrypted .shc file')
    run_parser.add_argument('file', help='Encrypted .shc file to run')
    run_parser.add_argument('-p', '--password', help='Decryption password (optional for passwordless files)')
    
    args = parser.parse_args()
    
    if args.command == 'encrypt':
        encrypt_file(args.input, args.output, args.password)
    elif args.command == 'run':
        run_encrypted_file(args.file, args.password)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
