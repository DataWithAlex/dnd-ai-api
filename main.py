from fastapi import FastAPI
from pydantic import BaseModel
import openai

from fastapi import FastAPI, HTTPException
import openai
import os

openai.api_key = "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"

app = FastAPI()

# Define a request model
class ChatRequest(BaseModel):
    text: str

@app.post("/chat/")
async def chat_with_openai(request: ChatRequest):
    #openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are going help me create a DND 5e character. When the user says 'Generate Character' that is when you are going to give all the relevant character info"},
            {"role": "user", "content": request.text}
        ]
    )
    content = response['choices'][0]['message']['content']
    return {"response": content}
