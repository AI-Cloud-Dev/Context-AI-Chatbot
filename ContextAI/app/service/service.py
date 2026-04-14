from groq import Groq
from typing import List
from app.model.model import ChatMessage
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in environment variables")

client = Groq(api_key=api_key)


def get_llm_response(messages: List[ChatMessage]) -> str:

    groq_messages = [
        {"role": msg.role, "content": msg.content}
        for msg in messages
    ]

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=groq_messages,
            temperature=0.3,
            max_tokens=1024   # 🔥 prevent huge responses
        )

        content = response.choices[0].message.content

        if not content:
            return "No response from model."

        return content.strip()

    except Exception as e:
        raise Exception(f"Groq API error: {str(e)}")
