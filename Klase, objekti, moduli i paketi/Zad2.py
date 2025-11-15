import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        if self.b == 0:
            print("Ne mogu dijelit s nulom")
            return None
        return self.a / self.b

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        if self.a < 0 or self.b < 0:
            print("Negativan broj -> nema korijena")
            return None
        return math.sqrt(self.a), math.sqrt(self.b)
k = Kalkulator(9, 16)
print("Zbroj:", k.zbroj())
print("Oduzimanje:", k.oduzimanje())
print("Mnozenje:", k.mnozenje())
print("Dijeljenje:", k.dijeljenje())
print("Potenciranje:", k.potenciranje())
print("Korijeni:", k.korijen())
