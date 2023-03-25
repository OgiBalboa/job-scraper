from httpx import AsyncClient
from enum import Enum
from pydantic import BaseModel


class JobFilter(BaseModel):
    name: str
    search_text: str | None = None
    easy_apply: bool | None = None


async def get_jobs_by_platform(platform_name: str, url_params: dict, **kwargs):
    url = PLATFORM_URLS[platform_name].format(url_params)
    async with AsyncClient() as client:
        await client.get(url, timeout=2 * 60, **kwargs)


class PlatformName(str, Enum):
    linkedin = 'linkedin'
    indeed = 'indeed'
    glassdoor = 'glassdoor'


PLATFORM_URLS = {
    'linkedin': 'https://linkedin.com/{param1}/{param2}'
}
