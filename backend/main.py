from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SYSTEM_PROMPT = """You are VedicBot, a knowledgeable assistant specializing in 
Vedic knowledge, Sanskrit texts, and ancient Indian wisdom. You have deep knowledge of:
- The four Vedas (Rigveda, Samaveda, Yajurveda, Atharvaveda)
- Upanishads, Bhagavad Gita, Mahabharata, Ramayana
- Sanskrit language and shlokas
- Vedic philosophy, Dharma, Karma, and Moksha
- Ayurveda, Yoga, and Vedic sciences

Always respond in the same language the user writes in.
When relevant, include a Sanskrit shloka or quote with its translation.
Be respectful, accurate, and insightful in your responses."""

chat_sessions = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"
    language: str = "english"

class ChatResponse(BaseModel):
    response: str
    session_id: str

@app.get("/")
def read_root():
    return {"status": "VedicBot is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if request.session_id not in chat_sessions:
        chat_sessions[request.session_id] = []

    history = chat_sessions[request.session_id]

    message = request.message
    if request.language.lower() != "english":
        message = f"Please respond in {request.language}. User message: {request.message}"

    history.append({"role": "user", "content": message})

    messages_to_send = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages_to_send,
        max_tokens=1024,
    )

    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    chat_sessions[request.session_id] = history

    return ChatResponse(
        response=reply,
        session_id=request.session_id
    )

@app.delete("/chat/{session_id}")
def clear_session(session_id: str):
    if session_id in chat_sessions:
        del chat_sessions[session_id]
    return {"status": "Session cleared"}