class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print("Naziv:", self.naziv,
              "| Cijena:", self.cijena, "eur",
              "| Dostupno:", self.dostupna_kolicina)

skladiste = [
    Proizvod("Mobitel", 1500, 5),
    Proizvod("Slušalice", 300, 20)
]

def dodaj_proizvod(podaci):
    """
    podaci je rječnik: {"naziv": ..., "cijena": ..., "dostupna_kolicina": ...}
    """
    novi = Proizvod(podaci["naziv"], podaci["cijena"], podaci["dostupna_kolicina"])
    skladiste.append(novi)
