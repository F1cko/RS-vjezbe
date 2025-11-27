import aiohttp
import asyncio
async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    async with session.get(url) as resp:
        data = await resp.json()
        try:
            return data["data"][0]["attributes"]["body"]
        except Exception:
            return str(data)


async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as resp:
        data = await resp.json()
        return data["fact"]


async def mix_facts(dog_facts, cat_facts):
    rezultat = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            rezultat.append(dog_fact)
        else:
            rezultat.append(cat_fact)
    return rezultat


async def main_zad3():
    async with aiohttp.ClientSession() as session:
        dog_tasks = [asyncio.create_task(get_dog_fact(session)) for _ in range(5)]
        cat_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)]

        dog_cat_facts = await asyncio.gather(*dog_tasks, *cat_tasks)

    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

    mixani = await mix_facts(dog_facts, cat_facts)

    print("Mixane činjenice o psima i mačkama:\n")
    for f in mixani:
        print(f)
if __name__ == "__main__":
    asyncio.run(main_zad3())
