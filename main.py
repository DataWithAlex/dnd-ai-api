from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Define a request model
class ChatRequest(BaseModel):
    text: str

@app.post("/chat/")
async def chat_with_openai(request: ChatRequest):
    # Retrieve the OpenAI API key from the environment variable
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are going help me create a DND 5e character. When the user says 'Generate Character' that is when you are going to give all the relevant character info"},
            {"role": "user", "content": request.text}
        ]
    )
    content = response['choices'][0]['message']['content']
    return {"response": content}
