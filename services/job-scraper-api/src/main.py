import asyncio
from typing import Annotated
from fastapi import FastAPI, Path, Query
from uuid import UUID

from utils.jobs import get_jobs_by_platform, PlatformName, PLATFORM_URLS, JobFilter

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is a job scraper api!"}


@app.get("/get-jobs/{filter-id}")
async def get_jobs(filter_id: int, platform: PlatformName | None = None):
    """Get jobs from platform(s) by filter id.
    :param filter_id: JobFilter model id. (platform_type of the filter must be universal
        if you don't specify platform name.
    :param platform: name of the platform.
    :return: list of the jobs returned by API endpoint.
    """
    if platform:
        return await get_jobs_by_platform(PLATFORM_URLS[platform], {})
    results = await asyncio.gather(
        *map(get_jobs_by_platform, PLATFORM_URLS.keys())
    )
    return results


@app.get("/job/filters/", response_model=list[JobFilter])
async def read_job_filter(
        id_: int = None,
        name: Annotated[
            str,
            Query(
                title='name',
                description='query job filters by name',
                min_length=1,
                max_length=55
            )
        ] = None,
        user_id: UUID = None
):
    return [{"id": id_, "name": name, "user_id": user_id}]


@app.post("/job/filters/")
async def create_job_filter(job_filter: JobFilter):
    return job_filter


@app.post("/job/filters/{job_filter_id}")
async def update_job_filter(
        job_filter_id: Annotated[int, Path(title='The ID of the item to get')],
        job_filter: JobFilter
):
    return job_filter
