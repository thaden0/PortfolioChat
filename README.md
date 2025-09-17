# AI ChatBot API

FastAPI-based REST API with local Ollama AI processing.

## Setup

1. **Install dependencies:**
```bash
python3 -m venv chatbot_env
source chatbot_env/bin/activate
pip install -r requirements.txt
```

2. **Install Ollama and pull model:**
```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull Qwen2.5 model
ollama pull hf.co/mradermacher/0824-Qwen2.5-0.5B-Instructt-16bit-3E-GGUF:Q3_K_S
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
- Model: Modify `Ollama(id="hf.co/mradermacher/0824-Qwen2.5-0.5B-Instructt-16bit-3E-GGUF:Q3_K_S")` in `api_chatbot.py`
- Knowledge: Update instructions in `api_chatbot.py`
