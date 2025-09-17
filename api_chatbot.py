from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agno.agent import Agent
from agno.models.ollama import Ollama
from datetime import datetime
import uvicorn
import os

# Initialize FastAPI app
app = FastAPI(
    title="Developer ChatBot API",
    description="API for Leonard Waugh Developer Information ChatBot",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()
EXPECTED_TOKEN = "EXPECTED_TOKEN"  # Same as in PHP consumer

# Request/Response Models
class ChatRequest(BaseModel):
    session: str
    message: str

class ChatResponse(BaseModel):
    session: str
    response: str
    timestamp: str
    status: str = "success"

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    service: str

# Initialize the agent (same as simple_chatbot.py)
agent = Agent(
    name="Developer Information ChatBot",
    model=Ollama(id="hf.co/mradermacher/0824-Qwen2.5-0.5B-Instructt-16bit-3E-GGUF:Q3_K_S"),
    instructions=[
        "You are a helpful assistant that answers questions about Leonard Waugh, a Senior Web and Software Engineer.",
        "",
        "## Leonard's Background:",
        "- Name: Leonard Waugh",
        "- Location: Tilbury, Ontario", 
        "- Experience: 33+ years in development",
        "- Specialization: Senior Web and Software Engineer",
        "",
        "## Work Experience:",
        "- Senior Full Stack Developer at Surex Insurance (2021–2025): Led Angular transitions, applied software architecture best practices",
        "- Software Developer II at United Shore (2019–2021): Contributed to large-scale projects, mentored new hires, worked in Kotlin and Swift",
        "- Software Development Manager at Clearcom Media (2013–2015): Oversaw team producing web and mobile applications",
        "- Software Developer at Flexxia: Worked in Drupal environment on medical industry webtools",
        "- Blackberry Technical Support: First tech job, developed templates using Spring with Java",
        "",
        "## Education:",
        "- Bachelor's Degree in Computer Science from University of Windsor (2015–2019)",
        "- Took many AI-related courses",
        "- Notable project: Genetic algorithm simulating population adapting to competitive environment",
        "",
        "## Programming Languages & Experience:",
        "- JavaScript/TypeScript: 15+ years experience, frameworks include Angular, React, Vue, jQuery",
        "- C# and ASP.NET: Used throughout United Shore time, includes Razor, Blazor, ASP.NET",
        "- PHP: Proficient with Laravel, Symfony, CodeIgniter, WordPress, Drupal",
        "- C++: 25+ years experience, used for tools, services, Unreal Engine 3D games",
        "- Python: Strong background, wrote chatbot using LangChain and FastAPI",
        "- Java: Proficient, made webapps with Spring and Spring Boot",
        "- Mobile: Kotlin, Swift, Flutter with Dart",
        "- CSS, SASS, LESS: 15+ years experience",
        "",
        "## Notable Projects:",
        "- Portal-like game for university final project (Unity, 2 weeks)",
        "- Minecraft mods for personal use",
        "- Aranea Platform (Laravel/Node/React)",
        "- Cyberscore Card: SEO audit service",
        "",
        "## Personal Interests:",
        "- Gaming: Plays Minecraft, PalWorld, CoreWars with wife Audrey",
        "- Outdoor: Kayaking and fishing on Lake St. Clair",
        "- Technology: Building drones, AI experimentation, autonomous systems",
        "- Pets: 4 cats - Makani, Dee, Harley, and Lucy",
        "",
        "## Current Focus:",
        "- Experimenting with LLM to simulate environments for storytelling and gaming",
        "- AI storytelling frameworks and autonomous systems",
        "- Local LLM hosting and LangChain integrations",
        "",
        "Provide clear, accurate, and helpful responses about Leonard's background, skills, experience, and projects.",
        "Use markdown formatting to make your responses more readable.",
        "If asked about something not covered above, politely say you don't have that information."
    ],
    markdown=True,
)

# Authentication dependency
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != EXPECTED_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials

# Health check endpoint (for isAvailable() method)
@app.get("/", response_model=HealthResponse)
async def health_check():
    """Health check endpoint for service availability"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        service="Developer ChatBot API"
    )

# Main chat endpoint (compatible with PHP consumer)
@app.post("/chat/messages", response_model=ChatResponse)
async def submit_message(request: ChatRequest, token: str = Depends(verify_token)):
    """
    Submit a message to the developer chatbot
    Compatible with PHP ChatService::submitMessage()
    """
    try:
        # Validate input
        if not request.message.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Message cannot be empty"
            )
        
        if not request.session.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Session cannot be empty"
            )
        
        # Get response from agent
        response = agent.run(request.message)
        response_content = response.content if hasattr(response, 'content') else str(response)
        
        return ChatResponse(
            session=request.session,
            response=response_content,
            timestamp=datetime.now().isoformat(),
            status="success"
        )
        
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log error and return error response
        print(f"ChatBot error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Chat service request failed: {str(e)}"
        )

# Additional endpoints for testing and debugging
@app.get("/chat/sessions/{session_id}")
async def get_session_info(session_id: str, token: str = Depends(verify_token)):
    """Get information about a chat session"""
    return {
        "session_id": session_id,
        "created_at": datetime.now().isoformat(),
        "status": "active"
    }

@app.get("/chat/health")
async def chat_health_check(token: str = Depends(verify_token)):
    """Health check for chat service specifically"""
    return {
        "status": "healthy",
        "service": "chat",
        "timestamp": datetime.now().isoformat(),
        "agent_status": "ready"
    }

if __name__ == "__main__":
    print("🚀 Starting Developer ChatBot API...")
    print("📡 API will be available at: http://127.0.0.1:8000")
    print("🔑 Authentication token: EXPECTED_TOKEN")
    print("📋 Main endpoint: POST /chat/messages")
    print("�� Health check: GET /")
    print("=" * 50)
    
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8000,
        log_level="info"
    )
