#!/bin/bash

# Rusthonian Super Project - Submodule Setup Script

echo "Setting up Rusthonian submodules..."

# Check if this is a git repository
if [ ! -d ".git" ]; then
    echo "Warning: This is not a Git repository."
    echo "To use Git submodules, first initialize this as a Git repository:"
    echo "  git init"
    echo "  git add ."
    echo "  git commit -m 'Initial commit'"
    echo ""
    echo "For now, the UUID module is available locally in the UUID/ directory."
    echo "You can build with UUID support using:"
    echo "  PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --features uuid"
    exit 0
fi

# Initialize submodules
echo "Initializing Git submodules..."
git submodule init

# Update submodules
echo "Updating Git submodules..."
git submodule update --init --recursive

# Add UUID submodule (if not already added)
if [ ! -d "UUID" ]; then
    echo "Adding UUID submodule..."
    git submodule add https://github.com/Rusthonian/UUID.git UUID
elif [ ! -f "UUID/.git" ]; then
    echo "UUID directory exists but is not a submodule."
    echo "To convert it to a submodule, you'll need to:"
    echo "1. Remove the UUID directory"
    echo "2. Run: git submodule add https://github.com/Rusthonian/UUID.git UUID"
fi

echo "Submodules setup complete!"
echo ""
echo "To build with UUID support:"
echo "  PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --features uuid"
