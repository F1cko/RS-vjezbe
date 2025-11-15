import math
class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * (self.r ** 2)


k1 = Krug(5)
print("Opseg kruga:", k1.opseg())
print("Površina kruga:", k1.povrsina())