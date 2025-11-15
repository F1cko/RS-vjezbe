class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print("Radim na poziciji", self.pozicija)

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        Radnik.__init__(self, ime, pozicija, placa)
        self.department = department

    def work(self):
        print("Radim na poziciji", self.pozicija, "u odjelu", self.department)

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(radnik.ime, "dobiva povisicu od", povecanje, "eur. Nova placa je", radnik.placa)


radnik1 = Radnik("Filip", "Skladistar", 1200)
manager1 = Manager("Ana", "Voditelj", 1800, "IT")
radnik1.work()
manager1.work()
manager1.give_raise(radnik1, 200)
