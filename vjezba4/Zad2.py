import aiohttp
import asyncio
async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as resp:
        data = await resp.json()
        return data["fact"] 

async def filter_cat_facts(facts):
    filtrirane = [
        fact for fact in facts
        if "cat" in fact.lower() or "cats" in fact.lower()
    ]
    return filtrirane

async def main_zad2():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]
        facts = await asyncio.gather(*tasks)

    filtrirane = await filter_cat_facts(facts)

    print("Filtrirane činjenice o mačkama:")
    for f in filtrirane:
        print("-", f)
if __name__ == "__main__":
    asyncio.run(main_zad2())
