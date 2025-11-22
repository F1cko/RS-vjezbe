import asyncio
baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]
async def autorizacija(korisnik_iz_baze, unesena_lozinka):
    await asyncio.sleep(2)

    zapis_lozinke = None
    for zapis in baza_lozinka:
        if zapis['korisnicko_ime'] == korisnik_iz_baze['korisnicko_ime']:
            zapis_lozinke = zapis
            break

    if zapis_lozinke is None:
        return "Korisnik " + korisnik_iz_baze['korisnicko_ime'] + ": lozinka nije pronađena u bazi."
    if zapis_lozinke['lozinka'] == unesena_lozinka:
        return "Korisnik " + korisnik_iz_baze['korisnicko_ime'] + ": Autorizacija uspješna."
    else:
        return "Korisnik " + korisnik_iz_baze['korisnicko_ime'] + ": Autorizacija neuspješna."


async def autentifikacija(korisnik):
    print("Pokrećem autentifikaciju za", korisnik['korisnicko_ime'])
    await asyncio.sleep(3)

    korisnik_iz_baze = None
    for k in baza_korisnika:
        if k['korisnicko_ime'] == korisnik['korisnicko_ime'] and k['email'] == korisnik['email']:
            korisnik_iz_baze = k
            break

    if korisnik_iz_baze is None:
        return "Korisnik " + korisnik['korisnicko_ime'] + " nije pronađen."
    rezultat_autorizacije = await autorizacija(korisnik_iz_baze, korisnik['lozinka'])
    return rezultat_autorizacije


async def main():
    korisnik_unos = {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'lozinka123'  
    }
    rezultat = await autentifikacija(korisnik_unos)
    print(rezultat)
asyncio.run(main())
