from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import questions, admin

app = FastAPI(title="SecPlus Quiz API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions.router, prefix="/api")
app.include_router(admin.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "SecPlus API is live"}