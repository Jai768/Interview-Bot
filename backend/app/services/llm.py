import requests
from dotenv import load_dotenv
import os
from backend.app.memory.llm_memory import conversation_history
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a professional technical interviewer."
}

def groq_chat_completion(session_id,message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    if session_id not in conversation_history:
        conversation_history[session_id] = [SYSTEM_PROMPT,]

    conversation_history[session_id].append({
        "role": "user",
        "content": message
    })

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": conversation_history[session_id]
    }
    try:
        response = requests.post(
            url,
            headers=headers,
            json=data
        )
        ai_message = response.json()["choices"][0]["message"]["content"]
        conversation_history[session_id].append({
            "role": "assistant",
            "content": ai_message
        })
        return ai_message
    except:
        return {"error": "Failed to connect to Groq API"}
