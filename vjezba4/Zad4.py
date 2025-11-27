import asyncio

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}
async def autentifikacija(korisnicko_ime, lozinka, simuliraj_timeout=False):
    await asyncio.sleep(2)

    if simuliraj_timeout:
        await asyncio.sleep(1)
        raise TimeoutError("Autentifikacijski servis ne radi.")
    if korisnicko_ime in korisnici and korisnici[korisnicko_ime] == lozinka:
        return f"{korisnicko_ime}: autentifikacija uspješna."
    else:
        raise ValueError(f"{korisnicko_ime}: neispravni podaci za prijavu.")


async def main_zad4():
    zahtjevi = [
        ("korisnik1", "lozinka1", False),
        ("korisnik2", "krivo", False),
        ("korisnik3", "lozinka3", False),
        ("korisnikX", "nesto", False),
        ("korisnik2", "lozinka2", True), 
    ]

    tasks = []
    for korisnicko_ime, lozinka, simuliraj_timeout in zahtjevi:
        task = asyncio.create_task(
            asyncio.wait_for(
                autentifikacija(korisnicko_ime, lozinka, simuliraj_timeout),
                timeout=3 
            )
        )
        tasks.append(task)
    rezultati = await asyncio.gather(*tasks, return_exceptions=True)

    for r in rezultati:
        if isinstance(r, asyncio.TimeoutError):
            print("Greška: globalni timeout pri autentifikaciji.")
        elif isinstance(r, TimeoutError):
            print("Greška: autentifikacijski servis ne radi:", r)
        elif isinstance(r, ValueError):
            print("Greška autentifikacije:", r)
        else:
            print("OK:", r)


if __name__ == "__main__":
    asyncio.run(main_zad4())
