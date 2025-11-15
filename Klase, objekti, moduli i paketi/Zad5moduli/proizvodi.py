class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina
skladiste = [
    Proizvod("Mobitelt", 1500, 5),
    Proizvod("Slušalice", 300, 20)
]