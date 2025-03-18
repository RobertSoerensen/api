from fastapi import FastAPI

app = FastAPI()


counterAPI = "/counter/v1"
@app.get(counterAPI + "/events")
async def getEvents():
    return {"message": "Events Success!"}