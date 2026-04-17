import json
from groq import Groq
from backend.config import Config

class GroqService:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = "llama-3.3-70b-versatile"

    def generate_exam_questions(self, objective_number: str, objective_title: str) -> list:
        prompt = f"""
You are a CompTIA Security+ SY0-701 certified exam question writer.

Generate exactly 15 multiple-choice questions for this exam objective:
Objective: {objective_number} — {objective_title}

Requirements:
- Mix difficulties: 5 easy, 5 medium, 5 hard
- Exam-realistic: scenario-based, "BEST", "MOST likely" phrasing
- 4 options per question (one correct)
- Short explanation (2-3 sentences) for correct answer

Respond ONLY with a valid JSON array, no markdown, no preamble:
[
  {{
    "question": "...",
    "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
    "correct_index": 0,
    "explanation": "...",
    "difficulty": "easy|medium|hard"
  }}
]
"""
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
            temperature=0.7, # Balanced for creativity and adherence to format
        )
        
        content = chat_completion.choices[0].message.content
        return content