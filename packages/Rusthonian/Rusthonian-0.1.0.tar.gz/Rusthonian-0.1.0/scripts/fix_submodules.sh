#!/bin/bash

# Fix missing submodules script for Rusthonian

echo "Fixing missing submodules..."

# Check if UUID directory is empty
if [ ! -f "UUID/Cargo.toml" ]; then
    echo "UUID submodule is missing. Initializing submodules..."
    git submodule update --init --recursive
    echo "Submodules initialized successfully!"
else
    echo "Submodules appear to be present."
fi

echo ""
echo "You can now build the project:"
echo "  PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --features uuid"
