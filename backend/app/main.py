import base64
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .ai_mock import ask_ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    repo_url: str
    question: str

class AskResponse(BaseModel):
    answer: str

def parse_github_repo(url: str):
    # Hỗ trợ dạng: https://github.com/owner/repo hoặc https://github.com/owner/repo.git
    try:
        parts = url.strip().split("/")
        owner = parts[3]
        repo = parts[4].replace(".git", "")
        return owner, repo
    except Exception:
        return None, None

async def fetch_readme(owner: str, repo: str):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    async with httpx.AsyncClient() as client:
        resp = await client.get(api_url)
        if resp.status_code != 200:
            return None
        data = resp.json()
        content = data.get("content")
        if not content:
            return None
        return base64.b64decode(content).decode("utf-8", errors="ignore")

@app.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    owner, repo = parse_github_repo(request.repo_url)
    if not owner or not repo:
        raise HTTPException(status_code=400, detail="repo_url không hợp lệ")
    readme = await fetch_readme(owner, repo)
    if not readme:
        raise HTTPException(status_code=404, detail="Không tìm thấy README")
    # Gửi nội dung tới AI (mock)
    answer = ask_ai(readme, request.question)
    return {"answer": answer}
