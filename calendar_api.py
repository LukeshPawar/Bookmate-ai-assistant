# 3. calendar_api.py - Google Calendar Integration

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_PATH = 'token.json'
CREDS_PATH = 'credentials.json'

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    else:
        raise Exception("Token file not found. Run auth script to generate token.json")
    return creds

def get_free_slots():
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=5, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        return "You're fully available!"
    response = "Your upcoming events:\n"
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        response += f"- {start}: {event['summary']}\n"
    return response

def book_calendar_slot(message):
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    start_time = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    end_time = start_time + datetime.timedelta(minutes=30)
    event = {
        'summary': 'BookMate Booking',
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Asia/Kolkata'}
    }
    event_result = service.events().insert(calendarId='primary', body=event).execute()
    return f"Booking confirmed: {event_result.get('htmlLink')}"
