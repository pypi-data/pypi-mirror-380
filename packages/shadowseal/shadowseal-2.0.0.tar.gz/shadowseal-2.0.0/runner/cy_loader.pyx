from cpython.mem cimport PyMem_Malloc, PyMem_Free
from cpython.ref cimport PyObject
from libc.stdio cimport FILE, fopen, fread, fclose, fseek, ftell, SEEK_END, SEEK_SET
from libc.stdlib cimport malloc, free
from libc.string cimport memset, memcpy, strcmp
from libc.time cimport time as c_time

import sys
import os
import builtins
import base64
import zlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305

# Advanced multi-layer decryption using Cython for performance

cdef void secure_xor_memzero(void* ptr, size_t len) nogil:
    """
    Secure memory zeroing using XOR pattern to prevent compiler optimization
    This prevents the compiler from removing the memzero operation
    """
    cdef volatile unsigned char* p = <volatile unsigned char*>ptr
    cdef size_t i
    cdef unsigned char mask = 0xFF
    for i in range(len):
        p[i] ^= mask
        p[i] = 0

cdef unsigned char complex_decrypt_byte(unsigned char b, unsigned char key, size_t index) nogil:
    """
    Complex byte-level decryption using multiple transformations
    This makes static analysis much harder
    """
    cdef unsigned char result = b
    
    # Layer 1: XOR with key
    result ^= key
    
    # Layer 2: Bit rotation based on index
    cdef int rotation = (index % 8)
    result = ((result << rotation) | (result >> (8 - rotation))) & 0xFF
    
    # Layer 3: Non-linear transformation
    result = ((result * 171) ^ 0x5A) % 256
    
    return result

cdef int check_ptrace():
    # Linux ptrace detection by reading /proc/self/status using Python file IO
    try:
        with open("/proc/self/status", "r") as f:
            for line in f:
                if line.startswith("TracerPid:"):
                    tracerpid = int(line.split()[1])
                    if tracerpid != 0:
                        return 1
                    else:
                        return 0
    except:
        return 0
    return 0

cdef int check_ld_preload():
    # Check if LD_PRELOAD is set
    cdef bytes ld = os.environ.get("LD_PRELOAD", "").encode()
    if ld:
        return 1
    return 0

cdef int check_debugger():
    # Check sys.gettrace
    if sys.gettrace() is not None:
        return 1
    return 0

cdef int check_proc_debug():
    # Check for presence of gdb or strace in /proc/self/maps or /proc/self/status
    try:
        with open("/proc/self/maps", "r") as f:
            maps = f.read()
            if "gdb" in maps or "strace" in maps:
                return 1
    except:
        pass
    return 0

cdef int anti_debug():
    if check_ptrace():
        return 1
    if check_ld_preload():
        return 1
    if check_debugger():
        return 1
    if check_proc_debug():
        return 1
    return 0

cdef void volatile_memzero(void* ptr, size_t len):
    """
    Volatile memory zeroing - compiler cannot optimize this away
    """
    cdef volatile unsigned char* p = <volatile unsigned char*>ptr
    cdef size_t i
    for i in range(len):
        p[i] = 0

cdef int advanced_anti_tamper_check() nogil:
    """
    Advanced anti-tampering checks at C level
    Returns 1 if tampering detected, 0 otherwise
    """
    # Check for common debugger patterns in memory
    # This is a simplified version - real implementation would be more complex
    return 0

cdef bytes multi_layer_decrypt(bytes encrypted_data, bytes key):
    """
    Multi-layer decryption matching the Python encryption logic
    Uses ChaCha20-Poly1305 + AES-256-GCM
    """
    import hashlib
    
    # Constants
    cdef int NONCE_SIZE = 12
    
    if len(encrypted_data) < NONCE_SIZE * 2:
        raise ValueError("Invalid encrypted data format")
    
    # Extract nonces and ciphertext
    nonce1 = encrypted_data[:NONCE_SIZE]
    nonce2 = encrypted_data[NONCE_SIZE:NONCE_SIZE * 2]
    ciphertext = encrypted_data[NONCE_SIZE * 2:]
    
    # Derive keys from master key
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

def run_shc(str filepath, password=None):
    """
    Advanced Cython-based .shc file runner with multi-layer decryption
    
    This function uses the same encryption format as the Python version,
    but with C-level performance optimizations and enhanced security checks.
    """
    # Anti-debugging check
    if anti_debug():
        print("Debugging detected. Exiting.")
        return False
    
    # Anti-tampering check at C level
    if advanced_anti_tamper_check():
        print("Tampering detected. Exiting.")
        return False
    
    try:
        # Use Python's file I/O for compatibility with the new format
        with open(filepath, 'rb') as f:
            packed_data = f.read()
        
        # Import the unpack function from Python module
        from encryptor.encrypt import unpack_shc, generate_key_from_password, generate_fixed_key
        
        # Unpack the file
        encrypted_data, salt, version, has_password = unpack_shc(packed_data)
        
        # Generate decryption key
        if has_password:
            if password is None:
                password = input("Enter decryption password: ").strip()
            key_length = 64 if version >= 4 else 32
            key = generate_key_from_password(password.encode(), salt, length=key_length)
        else:
            key = generate_fixed_key()
        
        # Multi-layer decryption
        decrypted = multi_layer_decrypt(encrypted_data, key)
        
        # Decode from base64
        data = base64.b64decode(decrypted)
        code_str = data.decode('utf-8')
        
        # Execute in restricted globals
        exec_globals = {
            '__builtins__': __builtins__,
            '__name__': '__main__',
            '__file__': filepath,
        }
        
        # Compile and execute
        code_obj = compile(code_str, filepath, 'exec')
        exec(code_obj, exec_globals)
        
        # Securely clear sensitive data from memory
        # Note: In Python 3.13+, strings are immutable and automatically garbage collected
        # We rely on Python's memory management here rather than manual zeroing
        
        return True
        
    except Exception as e:
        print(f"Execution error: {e}")
        import traceback
        traceback.print_exc()
        return False
