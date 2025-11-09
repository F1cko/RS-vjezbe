def provjera_lozinke(lozinka):

    if not 8 <= len(lozinka) <= 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return

    ima_veliko = False
    ima_broj = False

    for char in lozinka:
        if char.isupper():
            ima_veliko = True
        if char.isdigit():
            ima_broj = True

    if not (ima_veliko and ima_broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return

    lo = lozinka.lower()
    if "password" in lo or "lozinka" in lo:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return

    print("Lozinka je jaka!")

unesena = input("Unesi lozinku: ")
provjera_lozinke(unesena)
