#!/bin/bash

set -euo pipefail

curl -fsSL https://pyenv.run | bash

~/.pyenv/bin/pyenv install --skip-existing 3.13.7

# This script automates the installation of funstall on macOS and Linux.

# Define the target Python version and installation directories.
readonly PYTHON_VERSION="3.13.7"
readonly PYENV_ROOT_DIR="$HOME/software/python"
readonly VENV_DIR="$HOME/software/funstall"
readonly LOCAL_BIN_DIR="$HOME/.local/bin"

echo "Installing funstall"

mkdir -p "$LOCAL_BIN_DIR"

export PYENV_ROOT="$PYENV_ROOT_DIR"

if ! command -v pyenv &> /dev/null; then
  echo "-> pyenv not found. Installing now..."
  curl -fsSL https://pyenv.run | bash
fi

# Add pyenv to the PATH for the remainder of this script
export PATH="$PYENV_ROOT/bin:$PATH"

if ! pyenv versions --bare | grep -q "^${PYTHON_VERSION}$"; then
  pyenv install "$PYTHON_VERSION"
  echo "Python ${PYTHON_VERSION} installed."
fi

# TODO continue reivew

# Create a symlink for the python executable.
# The `%.*` removes the patch version (e.g., 3.13.0 -> 3.13).
PYTHON_EXECUTABLE_PATH="$PYENV_ROOT/versions/$PYTHON_VERSION/bin/python${PYTHON_VERSION%.*}"
SYMLINK_TARGET="$LOCAL_BIN_DIR/python${PYTHON_VERSION%.*}"
echo "-> Creating symlink from $PYTHON_EXECUTABLE_PATH to $SYMLINK_TARGET"
ln -sf "$PYTHON_EXECUTABLE_PATH" "$SYMLINK_TARGET"

# Step 4: Create a dedicated virtual environment for funstall.
echo "-> Setting up virtual environment at '$VENV_DIR'..."
if [ -d "$VENV_DIR" ]; then
    echo "-> Virtual environment directory already exists. Skipping creation."
else
    # Use the pyenv-provided python executable to create the venv.
    "$PYTHON_EXECUTABLE_PATH" -m venv "$VENV_DIR"
    echo "✅ Virtual environment created."
fi

# Step 5: Install funstall using the venv's pip.
echo "-> Installing 'funstall' package into the virtual environment..."
"$VENV_DIR/bin/pip" install --quiet --upgrade pip
"$VENV_DIR/bin/pip" install --quiet funstall
echo "✅ 'funstall' installed successfully."

# Step 6: Create a symlink to the funstall executable.
echo "-> Creating symlink for the 'funstall' executable..."
ln -sf "$VENV_DIR/bin/funstall" "$LOCAL_BIN_DIR/funstall"

echo ""
echo "🎉 Installation complete!"
echo "You can now run 'funstall' from your terminal."
echo "Make sure '$LOCAL_BIN_DIR' is in your shell's PATH."
