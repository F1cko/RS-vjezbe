import asyncio
import time
import aiohttp

async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as resp:
        return await resp.json()  
async def main_zad1():
    t1 = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_users(session)) for _ in range(5)]
        results = await asyncio.gather(*tasks)

    users = results[0]

    imena = [u["name"] for u in users]
    emailovi = [u["email"] for u in users]
    usernameovi = [u["username"] for u in users]

    t2 = time.perf_counter()
    print("Imena:", imena)
    print("Emailovi:", emailovi)
    print("Usernameovi:", usernameovi)
    print(f"Vrijeme izvođenja: {t2 - t1:.2f} sekundi")


if __name__ == "__main__":
    asyncio.run(main_zad1())
