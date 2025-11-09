def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])



def maks_i_min(lista):
    minimum = lista[0]
    maksimum = lista[0]

    for broj in lista:
        if broj < minimum:
            minimum = broj
        if broj > maksimum:
            maksimum = broj

    return (maksimum, minimum)


def presjek(s1, s2):
    novi = set()
    for element in s1:
        if element in s2:
            novi.add(element)
    return novi
print(prvi_i_zadnji([1,2,3,4,5,6,7,8,9,10]))      
print(maks_i_min([5,10,20,50,100,11,250,50,80]))   
print(presjek({1,2,3,4,5},{4,5,6,7,8}))            
