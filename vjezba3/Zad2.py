import asyncio
async def dohvati_korisnike():
    await asyncio.sleep(3)  
    korisnici = [
        {"ime": "Ivan", "email": "ivan@gmail.com"},
        {"ime": "Ana", "email": "ana@gmail.com"},
    ]
    print("Korisnici dohvaćeni.")
    return korisnici

async def dohvati_proizvode():
    await asyncio.sleep(5)  
    proizvodi = [
        {"naziv": "Laptop", "cijena": 7500},
        {"naziv": "Monitor", "cijena": 1200},
    ]
    print("Proizvodi dohvaćeni.")
    return proizvodi

async def main():
    korisnici, proizvodi = await asyncio.gather(
        dohvati_korisnike(),
        dohvati_proizvode()
    )
    print("\nRezultati:")
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)
asyncio.run(main())
