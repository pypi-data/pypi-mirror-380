"""
Data models for WeyCP Client
"""

from typing import List, Optional, Literal, Dict, Any
from dataclasses import dataclass


@dataclass
class Message:
    """Chat message"""
    role: Literal["system", "user", "assistant"]
    content: str
    
    def to_dict(self) -> Dict[str, str]:
        return {"role": self.role, "content": self.content}


@dataclass
class Usage:
    """Token usage information"""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class Choice:
    """Chat completion choice"""
    index: int
    message: Message
    finish_reason: Optional[str] = None


@dataclass
class ChatCompletion:
    """Chat completion response"""
    id: str
    object: str
    created: int
    model: str
    usage: Usage
    choices: List[Choice]


@dataclass
class ChatCompletionChunk:
    """Streaming chat completion chunk"""
    id: str
    object: str
    created: int
    model: str
    choices: List[Dict[str, Any]]


@dataclass
class HealthStatus:
    """Health check response"""
    status: str
    ollama_models: List[Dict[str, Any]]
    timestamp: str