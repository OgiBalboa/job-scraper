from datetime import datetime
from fastapi import FastAPI

from utils.jobs import get_jobs

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get-jobs/{start_date}")
async def get_jobs(start_date: datetime):
    if start_date == 'today':
        return await get_jobs(start_date=datetime.today().replace(hour=0, minute=0))
