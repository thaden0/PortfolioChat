#!/bin/bash

echo "�� Setting up AI ChatBot API..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv chatbot_env

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source chatbot_env/bin/activate

# Install dependencies
echo "📥 Installing Python dependencies..."
pip install -r requirements.txt

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama is not installed. Installing Ollama..."
    curl -fsSL https://ollama.ai/install.sh | sh
    echo "✅ Ollama installed. Please restart your terminal or run 'source ~/.bashrc'"
fi

# Pull required Ollama model
echo "🤖 Pulling Qwen2.5 model..."
ollama pull hf.co/mradermacher/0824-Qwen2.5-0.5B-Instructt-16bit-3E-GGUF:Q3_K_S

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the API server:"
echo "   source chatbot_env/bin/activate"
echo "   python api_chatbot.py"
echo ""
echo "📡 API will be available at: http://127.0.0.1:8000"
echo "🔑 Default token: EXPECTED_TOKEN"
