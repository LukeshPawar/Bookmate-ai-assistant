# 2. agent.py - LangGraph + NLP processor
import openai
import re
from calendar_api import get_free_slots, book_calendar_slot

async def process_user_message(message):
    # Basic intent extraction (simple rule-based fallback for now)
    if "available" in message or "free" in message:
        return get_free_slots()
    elif "book" in message or "schedule" in message:
        return book_calendar_slot(message)
    else:
        return "I'm not sure what you mean. Do you want to check availability or book a slot?"


 
