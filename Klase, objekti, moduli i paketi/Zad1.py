from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print("Marka:", self.marka)
        print("Model:", self.model)
        print("Godina proizvodnje:", self.godina_proizvodnje)
        print("Kilometraza:", str(self.kilometraza) + " km")

    def starost(self):
        trenutna = datetime.now().year
        star = trenutna - self.godina_proizvodnje
        print("Automobil je star", star, "godina")
auto = Automobil("Volkswagen", "Golf 7", 2015, 165000)
auto.ispis()
auto.starost()
