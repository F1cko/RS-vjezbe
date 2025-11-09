def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    count_v = 0
    count_c = 0

    for char in tekst:
        if char in vowels:
            count_v += 1
        elif char in consonants:
            count_c += 1

    return {"vowels": count_v, "consonants": count_c}


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))
