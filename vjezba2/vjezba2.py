unos_broja = input("Unesi broj telefona: ").strip()

def ocisti_broj(tekst_broja: str) -> str:
    dozvoljeni_znakovi = "+0123456789"
    return "".join(znak for znak in tekst_broja if znak in dozvoljeni_znakovi)

def u_nacionalni(oblik_broja: str) -> str:
    broj = ocisti_broj(oblik_broja)
    if broj.startswith("+"):
        broj = broj[1:]
    if broj.startswith("00385"):
        broj = broj[5:]
        if not broj.startswith("0"):
            broj = "0" + broj
    elif broj.startswith("385"):
        broj = broj[3:]
        if not broj.startswith("0"):
            broj = "0" + broj
    return broj

def rjecnik():
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
    return fiksne, mobilne, posebne

def samo_brojevi(tekst: str) -> bool:
    return len(tekst) > 0 and all("0" <= znak <= "9" for znak in tekst)

def pronadi_pozivni(nacionalni_broj: str):
    fiksne, mobilne, posebne = rjecnik()
    svi_prefiksi = list(fiksne) + list(mobilne) + list(posebne)
    svi_prefiksi.sort(key=len, reverse=True)
    for prefiks in svi_prefiksi:
        if nacionalni_broj.startswith(prefiks):
            if prefiks in fiksne:  return prefiks, "fiksna mreža",  fiksne[prefiks], None,            None
            if prefiks in mobilne: return prefiks, "mobilna mreža", None,            mobilne[prefiks], None
            if prefiks in posebne: return prefiks, "posebne usluge", None,           None,             posebne[prefiks]
    return None, None, None, None, None

def validiraj(broj_telefona: str) -> dict:
    nacionalni_broj = u_nacionalni(broj_telefona)
    pozivni_broj, vrsta_mreze, mjesto, operater, usluga = pronadi_pozivni(nacionalni_broj)
    if pozivni_broj is None:
        return {"pozivni_broj": None, "broj_ostatak": None, "vrsta": None, "mjesto": None, "operater": None, "usluga": None, "validan": False}
    ostatak_broja = nacionalni_broj[len(pozivni_broj):]
    if not samo_brojevi(ostatak_broja):
        return {"pozivni_broj": pozivni_broj, "broj_ostatak": None, "vrsta": vrsta_mreze, "mjesto": mjesto, "operater": operater, "usluga": usluga if vrsta_mreze=="posebne usluge" else None, "validan": False}
    if vrsta_mreze in ("fiksna mreža", "mobilna mreža"):
        ispravna_duljina = len(ostatak_broja) in (6, 7)
    else:
        ispravna_duljina = len(ostatak_broja) == 6
    return {
        "pozivni_broj": pozivni_broj,
        "broj_ostatak": ostatak_broja,
        "vrsta": vrsta_mreze,
        "mjesto": mjesto if vrsta_mreze == "fiksna mreža" else None,
        "operater": operater if vrsta_mreze == "mobilna mreža" else None,
        "usluga": usluga if vrsta_mreze == "posebne usluge" else None,
        "validan": ispravna_duljina,
    }

print(validiraj(unos_broja))
