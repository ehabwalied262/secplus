from fastapi import APIRouter, HTTPException
from typing import List
from backend.models.question import QuestionResponse
from backend.services.question_service import QuestionService
from backend.config import supabase_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/unverified", response_model=List[QuestionResponse])
async def get_unverified():
    """Fetches all questions that haven't been approved yet."""
    return QuestionService.get_unverified_questions()

@router.post("/verify/{question_id}")
async def verify_question(question_id: str):
    """Marks a specific question as verified."""
    try:
        supabase_admin.table("questions").update({"verified": True}).eq("id", question_id).execute()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))