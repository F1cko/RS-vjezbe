import asyncio
import random
async def fetch_weather_data(station_id):
    delay = random.uniform(1, 5)
    await asyncio.sleep(delay)

    temp = random.uniform(20, 25)
    print(f"Stanica {station_id}: {temp:.2f} °C (kašnjenje {delay:.2f} s)")
    return temp

async def safe_fetch_station(station_id, timeout=2):
    try:
        temp = await asyncio.wait_for(fetch_weather_data(station_id), timeout=timeout)
        return temp
    except asyncio.TimeoutError:
        print(f"Stanica {station_id}: Timeout (nije odgovorila na vrijeme).")
        return None
async def main_zad6():
    tasks = [asyncio.create_task(safe_fetch_station(i)) for i in range(1, 11)]
    rezultati = await asyncio.gather(*tasks)
    valjane_temp = [t for t in rezultati if t is not None]

    if valjane_temp:
        prosjek = sum(valjane_temp) / len(valjane_temp)
        print(f"\nProsječna temperatura (bez timeout stanica): {prosjek:.2f} °C")
    else:
        print("Nijedna stanica nije vratila podatke.")

if __name__ == "__main__":
    asyncio.run(main_zad6())
