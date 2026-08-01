import asyncio
import aiohttp

# syntax to use aiohttp is a little wierd, get used to it.
#
async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.json()   # <-- await and parse the JSON body
        print(f"Fetched {url} with status {response.status}")
        print(data["fact"])            # catfact.ninja returns {"fact": "...", "length": N}

async def main():
    urls = ["https://catfact.ninja/fact"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)
        # why this asterisk in *task: so there are 3 requests coming up in array
        # and we need to unpack them so the * syntax is helpful
        # putting just task won't well
        # syntax like this can also be used but it will be lengthy
        # tasks = [t1, t2, t3]
        # await asyncio.gather(t1,t2,t3)

asyncio.run(main())
