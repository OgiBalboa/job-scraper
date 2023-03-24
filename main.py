from datetime import datetime
from fastapi import FastAPI

from utils.jobs import get_jobs, PlatformName

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get-jobs/")
async def get_jobs(platform: PlatformName = None, start_date: datetime = None):
    if not start_date:
        start_date = datetime.today().replace(hour=0, minute=0)
    return await get_jobs(start_date=start_date, platform_name=platform)
