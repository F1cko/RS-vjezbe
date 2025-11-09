def obrni_rjecnik(rjecnik):
    novi = {}
    for kljuc, vrijednost in rjecnik.items():
        novi[vrijednost] = kljuc
    return novi

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))
