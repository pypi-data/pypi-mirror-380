#!/bin/bash
# ABOUTME: Script to build standalone binary executables for polyglot using PyInstaller
# ABOUTME: Creates platform-specific binaries that can be distributed without Python installed

set -e

echo "🔨 Building Polyglot standalone binary..."

# Install PyInstaller if not available
pip install pyinstaller --quiet

# Build the binary
pyinstaller \
    --name polyglot \
    --onefile \
    --console \
    --clean \
    polyglot_cli/__main__.py

echo "✅ Binary built successfully!"
echo "📦 Location: dist/polyglot"
echo ""
echo "To test:"
echo "  export ANTHROPIC_API_KEY='your-key'"
echo "  ./dist/polyglot translate python rust --file example.py"
