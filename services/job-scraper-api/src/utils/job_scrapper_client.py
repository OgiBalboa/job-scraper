import httpx


class BaseClient:
    def __init__(self):
        pass

    @staticmethod
    async def get_async(*args, **kwargs):
        async with httpx.AsyncClient() as client:
            return await client.get(*args, **kwargs)

    @staticmethod
    async def post_async(*args, **kwargs):
        async with httpx.AsyncClient() as client:
            return await client.post(*args, **kwargs)

    @staticmethod
    async def patch_async(*args, **kwargs):
        async with httpx.AsyncClient() as client:
            return await client.patch(*args, **kwargs)


class JobScrapperClient(BaseClient):
    job_ad_platform_configs = {
        'linked_in': {
            'url': '',
        }
    }

    def __init__(self):
        super().__init__()

    async def get_job_data(self, platform):
        config = self.job_ad_platform_configs[platform]
        await self.get_async(**config)

    def build_request_data(self, config):
        return {}
