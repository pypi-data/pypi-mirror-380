import os
import struct
import sys
import base64
from encryptor.encrypt import decrypt_data, unpack_shc, generate_key_from_password, generate_fixed_key
from utils.anti_debug import anti_debug
from utils.cross_platform import CrossPlatformManager

# Advanced loader with multi-layer decryption support

def run_shc(filepath, password=None):
    """Run an encrypted .shc file"""
    try:
        if anti_debug():
            print("Debugging detected. Exiting.")
            return False

        if not os.path.isfile(filepath):
            print(f"File not found: {filepath}")
            return False

        with open(filepath, 'rb') as f:
            packed_data = f.read()

        # Unpack and verify
        encrypted_data, salt, version, has_password = unpack_shc(packed_data)
        
        if has_password and password is None:
            # Prompt for password if not provided
            password = input("Enter decryption password: ").strip()
        
        if has_password:
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
        
        # Save original sys.argv and set it to the arguments after the .shc file
        original_argv = sys.argv[:]
        if len(sys.argv) > 2:
            # Remove 'shadowseal run' and the .shc file from sys.argv
            # Find the position of the .shc file
            shc_index = None
            for i, arg in enumerate(sys.argv):
                if arg.endswith('.shc') and os.path.isfile(arg):
                    shc_index = i
                    break
            
            if shc_index is not None:
                # Set sys.argv to start from the script arguments
                sys.argv = [filepath] + sys.argv[shc_index + 1:]
            else:
                # Fallback: just use the .shc file as first argument
                sys.argv = [filepath]
        else:
            # No additional arguments provided
            sys.argv = [filepath]
        
        try:
            code_obj = compile(code_str, filepath, 'exec')
            exec(code_obj, exec_globals)
        finally:
            # Restore original sys.argv
            sys.argv = original_argv
        return True

    except Exception as e:
        print(f"Execution error: {e}")
        return False

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Run encrypted .shc Python file')
    parser.add_argument('filepath', help='Path to the encrypted .shc file')
    parser.add_argument('-p', '--password', help='Decryption password (optional for passwordless files)')
    args = parser.parse_args()
    
    run_shc(args.filepath, args.password)

if __name__ == '__main__':
    main()
