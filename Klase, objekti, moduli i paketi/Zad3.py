class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    def prosjek(self):
        if len(self.ocjene) == 0:
            return 0
        return sum(self.ocjene) / len(self.ocjene)


studenti_podaci = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
studenti_objekti = []

for s in studenti_podaci:
    st = Student(s["ime"], s["prezime"], s["godine"], s["ocjene"])
    studenti_objekti.append(st)
najbolji_student = studenti_objekti[0]
for st in studenti_objekti:
    if st.prosjek() > najbolji_student.prosjek():
        najbolji_student = st

print("Najbolji student:", najbolji_student.ime, najbolji_student.prezime,
      "prosjek:", round(najbolji_student.prosjek(), 2))
