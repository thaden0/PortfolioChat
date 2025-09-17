# AI ChatBot API

FastAPI-based REST API with local Ollama AI processing.

## Setup

1. **Install dependencies:**
```bash
python3 -m venv chatbot_env
source chatbot_env/bin/activate
pip install -r requirements.txt
```

2. **Install Ollama and pull models:**
```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull required model
ollama pull llama3.2
```

3. **Run API:**
```bash
python api_chatbot.py
```

## API Usage

**Chat endpoint:**
```bash
curl -X POST "http://127.0.0.1:8000/chat/messages" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer EXPECTED_TOKEN" \
     -d '{"session": "test", "message": "Hello"}'
```

**Health check:**
```bash
curl http://127.0.0.1:8000/
```

## Configuration

- Token: Change `EXPECTED_TOKEN` in `api_chatbot.py`
- Model: Modify `Ollama(id="llama3.2")` in `api_chatbot.py`
- Knowledge: Update instructions in `api_chatbot.py`
