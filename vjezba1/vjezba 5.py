#Vjezba 5
#1 - nema smisla jer ide od 1 do 2 koji je isklucen pa ispise tako i tako 1
#2 #ispiše NIŠTA. (petlja se neće ni jednom izvršiti)
#310, 9, 8, 7, 6, 5, 4, 3, 2
suma = 0
for i in range(2, 101, 2):
    suma += i
print(suma)

neparni = []
for i in range(1, 20, 2):
    neparni.append(i)
neparni.reverse()
print(neparni)

a, b = 0, 1
while a <= 1000:
    print(a)
    a, b = b, a + b
