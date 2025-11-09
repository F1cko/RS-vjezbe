import random

trazeni_broj = random.randint(1, 100)
broj_je_pogoden = False
broj_pokusaja = 0

while not broj_je_pogoden:
    pokusaj = int(input("Unesi broj (1-100): "))
    broj_pokusaja += 1

    if pokusaj > trazeni_broj:
        print("Uneseni broj je veći od traženog.")
    elif pokusaj < trazeni_broj:
        print("Uneseni broj je manji od traženog.")
    else:
        broj_je_pogoden = True

print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")
