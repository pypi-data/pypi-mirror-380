#!/usr/bin/env python3
"""Post-installation script for Yoda CLI."""

import subprocess
import platform
import sys
from pathlib import Path


def print_banner():
    """Print welcome banner."""
    print("\n" + "="*60)
    print("🧙 Yoda CLI - Installation Complete!")
    print("="*60)


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print(f"⚠️  Warning: Python {version.major}.{version.minor} detected.")
        print("   Yoda requires Python 3.9 or higher for best compatibility.")
        return False
    return True


def check_homebrew():
    """Check if Homebrew is installed (macOS only)."""
    if platform.system() != "Darwin":
        return True

    try:
        result = subprocess.run(
            ['which', 'brew'],
            capture_output=True,
            timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False


def print_setup_info():
    """Print setup information."""
    system = platform.system()

    print("\n📦 Installation Summary:")
    print(f"   Platform: {system}")
    print(f"   Python: {sys.version.split()[0]}")

    if system == "Darwin":
        if check_homebrew():
            print("   Homebrew: ✓ Installed")
        else:
            print("   Homebrew: ✗ Not found")
            print("\n⚠️  Homebrew is recommended for automatic Ollama installation.")
            print("   Install from: https://brew.sh")

    print("\n🚀 Quick Start:")
    print("   1. Initialize a codebase:")
    print("      yoda init /path/to/your/project")
    print("\n   2. Generate README:")
    print("      yoda summarize")
    print("\n   3. Chat with your code:")
    print("      yoda chat")

    print("\n💡 What Happens on First Run:")
    print("   • Yoda will automatically install Ollama (if not present)")
    print("   • The Ollama service will start automatically")
    print("   • Required models will download on first use")
    print("   • This may take a few minutes the first time")

    if system not in ["Darwin", "Linux"]:
        print("\n⚠️  Windows users:")
        print("   Please install Ollama manually from https://ollama.com")
        print("   before running Yoda commands.")

    print("\n📚 Documentation:")
    print("   • README.md for detailed instructions")
    print("   • yoda --help for command options")

    print("\n" + "="*60)
    print("Happy coding with Yoda! 🎉")
    print("="*60 + "\n")


def main():
    """Main post-install function."""
    print_banner()

    if not check_python_version():
        print("\n⚠️  Please upgrade to Python 3.9 or higher.\n")
        sys.exit(1)

    print_setup_info()


if __name__ == "__main__":
    main()
