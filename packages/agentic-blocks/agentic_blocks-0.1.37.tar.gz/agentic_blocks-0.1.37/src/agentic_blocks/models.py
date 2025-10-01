"""
Request and response models for the agentic-blocks web API.
"""

from typing import List, Optional
from pydantic import BaseModel


class MessageFile(BaseModel):
    name: str
    type: str
    size: int
    url: Optional[str] = None


class MessagePart(BaseModel):
    type: str
    text: Optional[str] = None


class UIMessage(BaseModel):
    id: str
    role: str
    parts: Optional[List[MessagePart]] = None
    content: Optional[str] = None
    files: Optional[List[MessageFile]] = None


class ChatRequest(BaseModel):
    messages: List[UIMessage]
    model: str
    webSearch: bool = False
