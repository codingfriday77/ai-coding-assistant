from fastapi import FastAPI
from pydantic import BaseModel
from backend.utils import generate_code_from_prompt
from dotenv import load_dotenv
import os

# Load environment variables from .env file if it exists (local development)
# On Render, environment variables are set directly in the dashboard
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"), override=False)

app = FastAPI()

class CodeRequest(BaseModel):
    prompt: str
    language: str

@app.post("/generate_code")
def generate_code(request: CodeRequest):
    return {"code": generate_code_from_prompt(request.prompt, request.language)}
