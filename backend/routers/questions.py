from fastapi import APIRouter, HTTPException, Query
from typing import List
from models.question import QuestionResponse
from services.question_service import QuestionService

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.get("/", response_model=List[QuestionResponse])
async def get_quiz_questions(
    objective: str = Query(..., description="The exam objective number, e.g., 1.1"),
    limit: int = Query(10, ge=1, le=50)
):
    """
    Fetches verified questions for a specific exam objective.
    Used by the frontend quiz screen.
    """
    questions = QuestionService.get_verified_questions(objective, limit)
    if not questions:
        # Return an empty list if no verified questions are found yet
        return []
    return questions