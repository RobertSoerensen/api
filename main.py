from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests
from datetime import datetime

# Load environment variables from .env file e
load_dotenv()

app = FastAPI()

counterAPI = "/counter/v1"
@app.get(counterAPI + "/events")
async def getEvents():
    url = f"https://www.googleapis.com/calendar/v3/calendars/{os.getenv('COUNTER_CALENDAR_ID')}/events"
    params = {
        'timeMin': datetime.utcnow().isoformat() + 'Z',  # Ensure it's in UTC format
        'singleEvents': 'true',
        'orderBy': 'startTime',
        'key': os.getenv('COUNTER_API_KEY')
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    
    return data.get('items', [])