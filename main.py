from fastapi import FastAPI
import requests
from datetime import datetime

app = FastAPI()

# Counter Global variables
calendar_id = ""
api_key = ""

counterAPI = "/counter/v1"
@app.get(counterAPI + "/events")
async def getEvents():
    url = f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"
    params = {
        'timeMin': datetime.utcnow().isoformat() + 'Z',  # Ensure it's in UTC format
        'singleEvents': 'true',
        'orderBy': 'startTime',
        'key': api_key
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    
    return data.get('items', [])