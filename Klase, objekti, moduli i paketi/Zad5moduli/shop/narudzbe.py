from .proizvodi import skladiste
class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        dijelovi = []
        for p in self.naruceni_proizvodi:
            dio = p["naziv"] + " x " + str(p["narucena_kolicina"])
            dijelovi.append(dio)
        proizvodi_str = ", ".join(dijelovi)
        print("Naručeni proizvodi:", proizvodi_str + ", Ukupna cijena:", self.ukupna_cijena, "eur")
narudzbe = []


def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list):
        print("Greška: naruceni_proizvodi mora biti lista.")
        return None

    if len(naruceni_proizvodi) == 0:
        print("Greška: lista naručenih proizvoda je prazna.")
        return None
    
    potrebni_kljucevi = ["naziv", "cijena", "narucena_kolicina"]

    for p in naruceni_proizvodi:
        if not isinstance(p, dict):
            print("Greška: svaki element liste mora biti rječnik.")
            return None

        for kljuc in potrebni_kljucevi:
            if kljuc not in p:
                print("Greška: rječnik mora sadržavati ključeve: naziv, cijena, narucena_kolicina.")
                return None
            
    for p in naruceni_proizvodi:
        naziv = p["naziv"]
        kolicina = p["narucena_kolicina"]

        proizvod_u_skladistu = None
        for s in skladiste:
            if s.naziv == naziv:
                proizvod_u_skladistu = s
                break

        if proizvod_u_skladistu is None or proizvod_u_skladistu.dostupna_kolicina < kolicina:
            print("Proizvod", naziv, "nije dostupan!")
            return None

    for p in naruceni_proizvodi:
        naziv = p["naziv"]
        kolicina = p["narucena_kolicina"]
        for s in skladiste:
            if s.naziv == naziv:
                s.dostupna_kolicina -= kolicina
                break
    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in naruceni_proizvodi)

    narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append(narudzba)

    return narudzba
