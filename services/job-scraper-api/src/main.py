import asyncio
from fastapi import FastAPI

from utils.jobs import get_jobs_by_platform, PlatformName, PLATFORM_URLS

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is a job scraper api!"}


@app.get("/get-jobs/")
async def get_jobs(platform: PlatformName | None = None):
    if platform:
        return await get_jobs_by_platform(PLATFORM_URLS[platform], {})
    results = await asyncio.gather(
        *map(get_jobs_by_platform, PLATFORM_URLS.keys())
    )
    return results


@app.post("/job/filters")
async def upsert_job_filter(job_filter: JobFilter):
    pass