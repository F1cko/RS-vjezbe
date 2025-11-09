def brojanje_rijeci(tekst):
    rijeci = tekst.split()  
    ponavljanje = {}       

    for r in rijeci:
        if r in ponavljanje:
            ponavljanje[r] += 1
        else:
            ponavljanje[r] = 1

    return ponavljanje
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_rijeci(tekst))
