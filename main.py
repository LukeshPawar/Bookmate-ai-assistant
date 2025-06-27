# 1. main.py - FastAPI entry point
from fastapi import FastAPI, Request
from agent import process_user_message
from calendar_api import get_free_slots, book_calendar_slot

app = FastAPI()

@app.get("/")
def root():
    return {"message": "BookMate - AI Booking Assistant Running"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message")
    response = await process_user_message(user_input)
    return {"response": response}
