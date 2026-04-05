from fastapi import FastAPI
from pydantic import BaseModel
from backend.utils import generate_code_from_prompt
from dotenv import load_dotenv
import os

# Clear any cached API key and load fresh from .env
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"), override=True)

app = FastAPI()

class CodeRequest(BaseModel):
    prompt: str
    language: str

@app.post("/generate_code")
def generate_code(request: CodeRequest):
    return {"code": generate_code_from_prompt(request.prompt, request.language)}
