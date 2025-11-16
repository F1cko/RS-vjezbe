from shop import proizvodi
from shop import narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p)

print("Stanje skladišta:")
for p in proizvodi.skladiste:
    p.ispis()
naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Miš", "cijena": 100, "narucena_kolicina": 3}
]

print("\nPokušavam napraviti narudžbu...")
narudzba1 = narudzbe.napravi_narudzbu(naruceni_proizvodi)
if narudzba1:
    narudzba1.ispis_narudzbe()

    print("\nSve narudžbe:")
    for n in narudzbe.narudzbe:
        n.ispis_narudzbe()
