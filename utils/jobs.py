import asyncio
from httpx import AsyncClient


async def get_jobs_daily():
    return {}


async def get_job_by_platform(platform_name: str, url_params: dict, **kwargs):
    url = PLATFORM_URLS[platform_name].format(url_params)
    async with AsyncClient() as client:
        await client.get(url, timeout=2*60, **kwargs)


async def get_jobs(*, url_params: dict, start_date: str, end_date: str = None,):
    results = await asyncio.gather(
        *map(get_job_by_platform, PLATFORM_URLS.keys())
    )
    return results


PLATFORM_URLS = {
    'linkedin': 'https://linkedin.com/{param1}/{param2}'
}
