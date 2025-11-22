import asyncio
async def secure_data(podaci):
    await asyncio.sleep(3)
    enkriptirani = {
        "prezime": podaci["prezime"],
        "broj_kartice": hash(str(podaci["broj_kartice"])),
        "CVV": hash(str(podaci["CVV"]))
    }

    return enkriptirani
async def main():
    osjetljivi = [
        {"prezime": "Horvat", "broj_kartice": "4111111111111111", "CVV": "123"},
        {"prezime": "Sabolović", "broj_kartice": "5500000000000004", "CVV": "456"},
        {"prezime": "Kovač", "broj_kartice": "4000123412341234", "CVV": "789"}
    ]
    zadaci = [asyncio.create_task(secure_data(p)) for p in osjetljivi]

    rezultati = await asyncio.gather(*zadaci)
    print("\nEnkriptirani podaci:")
    for r in rezultati:
        print(r)

asyncio.run(main())
