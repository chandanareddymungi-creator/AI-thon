from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File upload route
@app.post("/upload")
async def upload_file(document: UploadFile = File(...)):
    content = await document.read()
    # In a real app, you'd process the file (e.g., extract text)
    return {"message": "File uploaded successfully", "filename": document.filename}

# Quiz generation route
@app.post("/generate-quiz")
async def generate_quiz():
    # Mock quiz response
    return {
        "quiz": "Q1: What is AI?\nA: Artificial Intelligence.",
        "analytics": "Score: 80% | Time: 5 mins",
        "recommendation": "Review: Chapter 3 - Neural Networks."
    }
