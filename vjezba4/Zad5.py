import asyncio
import aiohttp
async def fetch_url(session, url: str) -> str:
    async with session.get(url, timeout=5) as resp:
        return await resp.text()

async def main_zad5():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_url(session, url)) for url in urls]
        contents = await asyncio.gather(*tasks)

    for url, content in zip(urls, contents):
        print(f"Fetched {len(content)} characters from {url}")

if __name__ == "__main__":
    asyncio.run(main_zad5())
