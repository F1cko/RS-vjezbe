import asyncio
async def dohvati_podatke():
    await asyncio.sleep(3)

    podaci = [i for i in range(1, 11)]

    print("Podaci dohvaćeni.")
    return podaci


async def main():
    rezultat = await dohvati_podatke()
    print("Rezultat:", rezultat)
asyncio.run(main())
