from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class QuestionBase(BaseModel):
    domain_number: str
    domain_title: str
    question: str
    options: List[str]
    correct_index: int
    explanation: str
    difficulty: str = Field(pattern="^(easy|medium|hard)$")

class QuestionCreate(QuestionBase):
    verified: bool = False

class QuestionUpdate(BaseModel):
    question: Optional[str] = None
    options: Optional[List[str]] = None
    correct_index: Optional[int] = None
    explanation: Optional[str] = None
    difficulty: Optional[str] = None
    verified: Optional[bool] = None

class QuestionResponse(QuestionBase):
    id: UUID
    verified: bool
    created_at: datetime

    class Config:
        from_attributes = True
