import os
import sys
from setuptools import setup, Extension, find_packages

# Try to import Cython, but don't fail if not available
try:
    from Cython.Build import cythonize
    HAS_CYTHON = True
except ImportError:
    HAS_CYTHON = False
    cythonize = None

def read_requirements():
    """Read requirements from requirements.txt"""
    try:
        with open('requirements.txt') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        return ['cython>=3.0', 'cryptography>=41.0.0', 'psutil>=5.8.0']

def check_android_environment():
    """Check if running in Android/Termux environment"""
    try:
        # Check for Android-specific indicators
        if os.path.exists("/system/build.prop") or os.path.exists("/system/bin/getprop"):
            return True
        if "TERMUX" in os.environ.get("PREFIX", ""):
            return True
        return False
    except:
        return False

# Check if we're in Android environment
is_android = check_android_environment()

# Configure extensions based on platform - now more flexible
extensions = []

# Only build Cython extensions if:
# 1. Cython is available
# 2. Not on Android
# 3. Not explicitly disabled via environment variable
# 4. C compiler is available (we'll let setuptools handle this gracefully)
if HAS_CYTHON and not is_android and not os.environ.get('SHADOWSEAL_NO_CYTHON'):
    try:
        # Build Cython extensions for better performance on supported platforms
        extensions = [
            Extension("runner.cy_loader", ["runner/cy_loader.pyx"])
        ]
    except Exception:
        # If anything goes wrong, fall back to pure Python
        extensions = []
else:
    # Use pure Python fallback
    extensions = []

setup(
    name="shadowseal",
    version="2.0.0",
    description="Advanced multi-layer Python encryption with ChaCha20-Poly1305 + AES-256-GCM and cross-platform support",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author="Monarch of Shadows",
    author_email="farhanbd637@gmail.com",
    url="https://github.com/AFTeam-Owner/shadowseal",
    packages=find_packages(),
    install_requires=read_requirements(),
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.8',
            'mypy>=0.800',
        ],
        'android': [
            'psutil>=5.8.0',
        ],
    },
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}) if (extensions and HAS_CYTHON) else [],
    entry_points={
        "console_scripts": ["shadowseal=shadowseal.cli:main"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Systems Administration",
    ],
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
    keywords='encryption, obfuscation, security, python, anti-debugging, android, termux',
)
