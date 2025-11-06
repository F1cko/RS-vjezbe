
broj = input("Unesi broj telefona: ")

def dct_pozivni():
    fiksne = {
        "01": "Grad Zagreb i Zagrebačka županija",
        "020": "Dubrovačko-neretvanska županija",
        "021": "Splitsko-dalmatinska županija",
        "022": "Šibensko-kninska županija",
        "023": "Zadarska županija",
        "031": "Osječko-baranjska županija",
        "032": "Vukovarsko-srijemska županija",
        "033": "Virovitičko-podravska županija",
        "034": "Požeško-slavonska županija",
        "035": "Brodsko-posavska županija",
        "040": "Međimurska županija",
        "042": "Varaždinska županija",
        "043": "Bjelovarsko-bilogorska županija",
        "044": "Sisačko-moslavačka županija",
        "047": "Karlovačka županija",
        "048": "Koprivničko-križevačka županija",
        "049": "Krapinsko-zagorska županija",
        "051": "Primorsko-goranska županija",
        "052": "Istarska županija",
        "053": "Ličko-senjska županija",
    }
    mobilne = {
        "091": "A1 Hrvatska",
        "092": "Tomato",
        "095": "Telemach",
        "097": "bonbon",
        "098": "Hrvatski Telekom",
        "099": "Hrvatski Telekom",
    }
    posebne = {
        "0800": "Besplatni pozivi",
        "060": "Komercijalni pozivi",
        "061": "Glasovanje telefonom",
        "064": "Usluge s neprimjerenim sadržajem",
        "065": "Nagradne igre",
        "069": "Usluge namijenjene djeci",
        "072": "Jedinstveni pristupni broj za cijelu državu za posebne usluge",
    }
    print(broj)