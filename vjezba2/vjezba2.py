broj = input("Unesi broj telefona: ").strip()

def ocisti(b: str) -> str:
    doz = "+0123456789"
    return "".join(ch for ch in b if ch in doz)

def norm(b: str) -> str:
    b = ocisti(b)
    if b.startswith("+"): b = b[1:]
    if b.startswith("00385"):
        b = b[5:];  b = b if b.startswith("0") else "0"+b
    elif b.startswith("385"):
        b = b[3:];  b = b if b.startswith("0") else "0"+b
    return b

def rjecnik():
    fiks = {
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
    mob = {
        "091": "A1 Hrvatska",
        "092": "Tomato",
        "095": "Telemach",
        "097": "bonbon",
        "098": "Hrvatski Telekom",
        "099": "Hrvatski Telekom",
    }
    spec = {
        "0800":"Besplatni pozivi",
        "060": "Komercijalni pozivi",
        "061": "Glasovanje telefonom",
        "064": "Usluge s neprimjerenim sadržajem",
        "065": "Nagradne igre",
        "069": "Usluge namijenjene djeci",
        "072": "Jedinstveni pristupni broj za cijelu državu za posebne usluge",
    }
    return fiks, mob, spec

def samo_brojevi(s: str) -> bool:
    return len(s)>0 and all("0"<=c<="9" for c in s)

def find_poz(b: str):
    fiks, mob, spec = rjecnik()
    svi = list(fiks)+list(mob)+list(spec)
    svi.sort(key=len, reverse=True)
    for p in svi:
        if b.startswith(p):
            if p in fiks: return p,"fiksna mreža",fiks[p],None
            if p in mob:  return p,"mobilna mreža",None,mob[p]
            if p in spec: return p,"posebne usluge",None,None
    return None,None,None,None

def validiraj(broj: str) -> dict:
    b = norm(broj)
    poz, vrsta, mjesto, oper = find_poz(b)
    if poz is None:
        return {"pozivni_broj":None,"broj_ostatak":None,"vrsta":None,"mjesto":None,"operater":None,"validan":False}
    ost = b[len(poz):]
    if not samo_brojevi(ost):
        return {"pozivni_broj":poz,"broj_ostatak":None,"vrsta":vrsta,"mjesto":mjesto,"operater":oper,"validan":False}
    if vrsta in ("fiksna mreža","mobilna mreža"):
        ok = len(ost) in (6,7)
    else:
        ok = len(ost)==6
    return {"pozivni_broj":poz,"broj_ostatak":ost,"vrsta":vrsta,"mjesto":mjesto if vrsta=="fiksna mreža" else None,"operater":oper if vrsta=="mobilna mreža" else None,"validan":ok}

print(validiraj(broj))
