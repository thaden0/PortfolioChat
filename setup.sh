#!/bin/bash

# Developer ChatBot Setup Script

echo "🤖 Setting up Developer ChatBot..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed. Please install Ollama from https://ollama.com/download"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Start Qdrant vector database
echo "🗄️ Starting Qdrant vector database..."
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant

# Wait for Qdrant to start
echo "⏳ Waiting for Qdrant to start..."
sleep 5

# Pull required Ollama models
echo "🦙 Pulling Ollama models..."
ollama pull llama3.2
ollama pull openhermes

echo "✅ Setup complete!"
echo ""
echo "🚀 To start the chatbot, run:"
echo "   python developer_chatbot.py"
echo ""
echo "📝 Make sure to update developer_info.txt with your actual developer information"
