def ukloni_duplikate(lista):
    pomocni_skup = set()     
    nova_lista = []

    for element in lista:
        if element not in pomocni_skup:
            pomocni_skup.add(element)
            nova_lista.append(element)

    return nova_lista
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))
