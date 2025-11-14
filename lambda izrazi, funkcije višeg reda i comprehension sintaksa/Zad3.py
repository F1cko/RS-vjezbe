import math
parni_kvadrati = [x ** 2 for x in range(20, 51) if x % 2 == 0]
print(parni_kvadrati)

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
duljine_sa_slovom_a = [len(r) for r in rijeci if "a" in r]
print(duljine_sa_slovom_a)

kubovi = [{i: (i ** 3 if i % 2 != 0 else i)} for i in range(1, 11)]
print(kubovi)



korijeni = {x: round(math.sqrt(x), 2) for x in range(50, 501, 50)}
print(korijeni)
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
zbrojeni_bodovi = [{s["prezime"]: sum(s["bodovi"])} for s in studenti]
print(zbrojeni_bodovi)

faktorijeli = {
    i: [math.factorial(j) for j in range(1, i + 1)]
    for i in range(1, 11)
}

print(faktorijeli)