import asyncio
import json
import logging
import os
import time
from typing import List, Dict, Any, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

from agentic_blocks.agent import Agent
from agentic_blocks.models import ChatRequest
from agentic_blocks.utils.server_utils import extract_message_content
from agno.tools import tool

# Setup
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env.local"))
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Elements FastAPI Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    return HTTPException(status_code=422, detail=f"Validation error: {exc.errors()}")


# Request Models are now imported from shared module


# Math Tools
@tool
def add(a: float, b: float) -> float:
    """Adds a and b.

    Args:
        a: first number
        b: second number
    """
    return a + b


@tool
def multiply(a: float, b: float) -> float:
    """Multiplies a and b.

    Args:
        a: first number
        b: second number
    """
    return a * b


# extract_message_content is now imported from utils.server_utils

async def generate_ui_message_stream(request: ChatRequest):
    """Generate streaming response using Agent class."""
    logger.info(f"Starting chat - {len(request.messages)} messages")

    try:
        # Extract the latest user message
        user_message = ""
        for ui_msg in reversed(request.messages):
            if ui_msg.role == "user":
                user_message = extract_message_content(ui_msg)
                break

        if not user_message:
            user_message = "Hello"

        # Create agent with tools
        system_prompt = "You are a helpful assistant that can perform mathematical calculations. You have access to 'add' and 'multiply' tools for arithmetic operations. When users ask for calculations, use these tools to provide accurate results."
        agent = Agent(system_prompt=system_prompt, tools=[add, multiply])

        # Stream response using agent
        async for sse_event in agent.run_stream_sse(user_message):
            yield sse_event
            # Force flush to prevent buffering
            await asyncio.sleep(0.01)

        logger.info("Chat completed")

    except Exception as e:
        logger.error(f"Error in chat stream: {str(e)}", exc_info=True)
        yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"


# API Endpoints
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """Chat endpoint compatible with AI SDK useChat hook."""
    logger.info(f"Chat request: {request.model}, {len(request.messages)} messages")

    # Validate API key
    try:
        from agentic_blocks.utils.config_utils import get_llm_config
        config = get_llm_config()
        if not config.get("api_key"):
            raise HTTPException(status_code=500, detail="API key not configured. Set OPENROUTER_API_KEY or OPENAI_API_KEY.")
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return StreamingResponse(
        generate_ui_message_stream(request),
        media_type="text/plain; charset=utf-8",
        headers={
            "x-vercel-ai-ui-message-stream": "v1",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        from agentic_blocks.utils.config_utils import get_llm_config
        api_key_configured = bool(get_llm_config().get("api_key"))
    except (ValueError, ImportError):
        api_key_configured = False

    return {
        "status": "healthy",
        "timestamp": time.time(),
        "api_key_configured": api_key_configured
    }

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "AI Elements FastAPI Backend", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
