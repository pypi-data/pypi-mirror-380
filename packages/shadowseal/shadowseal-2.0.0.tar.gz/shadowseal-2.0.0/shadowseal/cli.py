import argparse
import sys
import os
from encryptor import encrypt
from runner import loader

# Fix encoding for Windows console
if sys.platform == 'win32':
    try:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'replace')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'replace')
    except:
        pass  # If it fails, continue without UTF-8 support

def main():
    parser = argparse.ArgumentParser(
        description="ShadowSeal - Advanced Multi-Layer Python Encryption Tool",
        usage="shadowseal {encrypt,run} ...\n"
              "  shadowseal encrypt <script>.py [-o <output>.shc] [-p <password>]\n"
              "  shadowseal run <script>.shc [-p <password>]\n\n"
              "Advanced Features:\n"
              "  • Multi-layer encryption: ChaCha20-Poly1305 + AES-256-GCM\n"
              "  • PBKDF2-HMAC-SHA512 with 600,000 iterations\n"
              "  • Hardware-bound encryption (no password mode)\n"
              "  • Cross-platform compatibility (Windows/Linux/macOS/Android/iOS)\n"
              "  • Irreversible encryption - decryption not supported"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a Python file')
    encrypt_parser.add_argument('input', help='Input Python (.py) file to encrypt')
    encrypt_parser.add_argument('-o', '--output', required=True, help='Output encrypted .shc file')
    encrypt_parser.add_argument('-p', '--password', help='Encryption password (optional - passwordless if not provided)')

    # Run command
    run_parser = subparsers.add_parser('run', help='Run an encrypted .shc file',
                                      usage="shadowseal run <script>.shc [-p PASSWORD] [-- script_args...]")
    run_parser.add_argument('file', help='Encrypted .shc file to run')
    run_parser.add_argument('-p', '--password', help='Decryption password (optional for passwordless files)')
    run_parser.add_argument('script_args', nargs=argparse.REMAINDER, help='Arguments to pass to the encrypted script')

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    if args.command == 'encrypt':
        print(f"🔐 Encrypting {args.input} to {args.output}...")
        print(f"⚡ Using advanced multi-layer encryption (ChaCha20-Poly1305 + AES-256-GCM)")
        password = encrypt.encrypt_file(args.input, args.output, args.password)
        if args.password is None:
            print("✅ Encryption complete (hardware-bound, no password required)")
        else:
            print("✅ Encryption complete (password-protected)")
            print(f"🔑 Password: {password}")
        print("\n📋 Usage:")
        print(f"  shadowseal run {args.output}")
        print("\n⚠️  Note: Decryption back to source code is NOT supported.")
        print("⚠️  This is an irreversible encryption designed for maximum security.")

    elif args.command == 'run':
        print(f"💥 Running encrypted file: {args.file}")
        success = loader.run_shc(args.file, args.password)
        if success:
            print("✅ Execution completed successfully")
        else:
            print("❌ Execution failed")
            sys.exit(1)

if __name__ == '__main__':
    main()
