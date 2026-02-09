#!/bin/bash
echo "Installing System Dependencies for AETHER Project..."

# Update System
sudo apt-get update && sudo apt-get install -y \
    git wget curl build-essential \
    ffmpeg tesseract-ocr libtesseract-dev \
    cmake protobuf-compiler

# Install Ollama (Linux/WSL)
if ! command -v ollama &> /dev/null; then
    curl -fsSL https://ollama.com/install.sh | sh
fi

# Clone specific Repos if needed (Example: AUTOMATIC1111)
# git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

echo "System tools installed successfully."
