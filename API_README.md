# 🤖 Developer ChatBot API

A FastAPI-based REST API for Leonard Waugh's Developer Information ChatBot, compatible with PHP consumers.

## 🚀 Features

- **PHP Compatible**: Designed to work with Laravel's HTTP client
- **Bearer Token Authentication**: Secure API access
- **Session Management**: Track conversations by session ID
- **Error Handling**: Proper HTTP status codes and error messages
- **Health Checks**: Service availability monitoring
- **CORS Support**: Cross-origin requests enabled

## 📡 API Endpoints

### Health Check
```http
GET /
```
**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00",
  "service": "Developer ChatBot API"
}
```

### Chat Messages
```http
POST /chat/messages
```

**Headers:**
```
Content-Type: application/json
Authorization: Bearer EXPECTED_TOKEN
```

**Request Body:**
```json
{
  "session": "user-session-123",
  "message": "What programming languages does Leonard know?"
}
```

**Response:**
```json
{
  "session": "user-session-123",
  "response": "Leonard knows JavaScript/TypeScript (15+ years), C#/ASP.NET, PHP, C++ (25+ years), Python, Java, and mobile languages like Kotlin and Swift...",
  "timestamp": "2024-01-15T10:30:00",
  "status": "success"
}
```

### Additional Endpoints

- `GET /chat/sessions/{session_id}` - Get session information
- `GET /chat/health` - Chat service health check

## 🔧 Setup & Installation

### 1. Install Dependencies
```bash
cd /home/len/code/agent/chatbot
source chatbot_env/bin/activate
pip install fastapi uvicorn requests
```

### 2. Start Qdrant (if using knowledge base)
```bash
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
```

### 3. Install Ollama Models
```bash
ollama pull llama3.2
ollama pull openhermes
```

### 4. Run the API Server
```bash
python api_chatbot.py
```

The API will be available at: `http://127.0.0.1:8000`

## 🧪 Testing

### Run Test Suite
```bash
python test_api.py
```

### Manual Testing with curl
```bash
# Health check
curl http://127.0.0.1:8000/

# Chat message
curl -X POST "http://127.0.0.1:8000/chat/messages" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer EXPECTED_TOKEN" \
     -d '{"session": "test-session", "message": "What is Leonard's background?"}'
```

## 🔐 Authentication

The API uses Bearer token authentication. Set the token in your PHP consumer:

```php
private const AUTH_TOKEN = 'EXPECTED_TOKEN';
```

## 📋 PHP Consumer Compatibility

This API is designed to work seamlessly with the provided PHP ChatService:

```php
$chatService = new ChatService();
$response = $chatService->submitMessage('user-session-123', 'What programming languages does Leonard know?');
```

### Expected Behavior:
- ✅ `isAvailable()` method works with `GET /`
- ✅ `submitMessage()` method works with `POST /chat/messages`
- ✅ Proper error handling and HTTP status codes
- ✅ JSON response format matches expectations

## 🛠️ Configuration

### Environment Variables
- `EXPECTED_TOKEN`: Authentication token (default: "EXPECTED_TOKEN")
- `OLLAMA_MODEL`: Ollama model to use (default: "llama3.2")

### Customization
- Modify `agent.instructions` in `api_chatbot.py` to change Leonard's information
- Update `EXPECTED_TOKEN` for security
- Change port/host in `uvicorn.run()` if needed

## 🚨 Error Handling

The API returns appropriate HTTP status codes:

- `200`: Success
- `400`: Bad Request (empty message/session)
- `401`: Unauthorized (invalid token)
- `500`: Internal Server Error (agent/ollama issues)

## 📊 Monitoring

### Health Checks
- `GET /` - Basic service health
- `GET /chat/health` - Chat service specific health

### Logging
The API logs all requests and errors to console. For production, configure proper logging.

## 🔄 Deployment

### Development
```bash
python api_chatbot.py
```

### Production (with Gunicorn)
```bash
pip install gunicorn
gunicorn api_chatbot:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker (Optional)
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "api_chatbot.py"]
```

## 🎯 Usage Examples

### Ask about Leonard's Experience
```json
{
  "session": "session-1",
  "message": "Tell me about Leonard's work experience"
}
```

### Ask about Skills
```json
{
  "session": "session-1", 
  "message": "What programming languages does Leonard know?"
}
```

### Ask about Projects
```json
{
  "session": "session-1",
  "message": "What notable projects has Leonard worked on?"
}
```

The API will respond with detailed, formatted information about Leonard Waugh based on the knowledge base.
