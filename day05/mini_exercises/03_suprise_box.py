# Uvozimo random, da lahko računalnik naključno izbira iz seznamov
import random


# =========================
# ASCII NASLOV
# =========================

print(r"""
__        __   _                          _ 
 \ \      / /__| | ___ ___  _ __ ___   ___| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)

        ŽIVILA PRESENEČENJA

""")


# =========================
# SEZNAMI ŽIVIL
# =========================

# Seznam sadja
sadje = [
    "jabolko", "banana", "pomaranca", "jagoda", "grozdje",
    "kivi", "ananas", "breskev", "hruska", "limona"
]

# Seznam zelenjave
zelenjava = [
    "korenje", "krompir", "paradiznik", "kumara", "solata",
    "paprika", "čebula", "brokoli", "cvetača", "bučka"
]

# Seznam mesa
meso = [
    "piščanec", "govedina", "svinjina", "puran", "jagnjetina",
    "raca", "slanina", "klobasa", "pršut", "čevapčiči"
]

# Seznam sladkarij
sladkarije = [
    "čokolada", "bonboni", "lizika", "piškoti", "torta",
    "sladoled", "krofi", "vaflji", "muffin", "karamela"
]


# =========================
# PRAZEN NAKUPOVALNI VOZIČEK
# =========================

# Sem bomo dodajali naključna živila
nakupovalni_vozicek = []


# =========================
# VPRAŠANJA ZA UPORABNIKA
# =========================

# Uporabnik izbere, koliko živil želi iz vsake skupine
st_sadje = int(input("Koliko naključnega sadja želiš: "))
st_zelenjava = int(input("Koliko naključne zelenjave želiš: "))
st_meso = int(input("Koliko naključnega mesa želiš: "))
st_sladkarije = int(input("Koliko naključnih sladkarij želiš: "))


# =========================
# NAKLJUČNO SADJE
# =========================

# Dodajamo sadje, dokler ga ni toliko, kot je uporabnik želel
while len(nakupovalni_vozicek) < st_sadje:
    nakljucni_nakup = random.choice(sadje)

    # Dodamo samo, če tega živila še ni v vozičku
    if nakljucni_nakup not in nakupovalni_vozicek:
        nakupovalni_vozicek.append(nakljucni_nakup)


# =========================
# NAKLJUČNA ZELENJAVA
# =========================

# Dodajamo zelenjavo za sadjem
while len(nakupovalni_vozicek) < st_sadje + st_zelenjava:
    nakljucni_nakup = random.choice(zelenjava)

    # Dodamo samo, če tega živila še ni v vozičku
    if nakljucni_nakup not in nakupovalni_vozicek:
        nakupovalni_vozicek.append(nakljucni_nakup)


# =========================
# NAKLJUČNO MESO
# =========================

# Dodajamo meso za sadjem in zelenjavo
while len(nakupovalni_vozicek) < st_sadje + st_zelenjava + st_meso:
    nakljucni_nakup = random.choice(meso)

    # Dodamo samo, če tega živila še ni v vozičku
    if nakljucni_nakup not in nakupovalni_vozicek:
        nakupovalni_vozicek.append(nakljucni_nakup)


# =========================
# NAKLJUČNE SLADKARIJE
# =========================

# Dodajamo sladkarije na koncu
while len(nakupovalni_vozicek) < st_sadje + st_zelenjava + st_meso + st_sladkarije:
    nakljucni_nakup = random.choice(sladkarije)

    # Dodamo samo, če tega živila še ni v vozičku
    if nakljucni_nakup not in nakupovalni_vozicek:
        nakupovalni_vozicek.append(nakljucni_nakup)


# =========================
# PREMEŠAJ VOZIČEK
# =========================

# Premešamo vrstni red živil v vozičku
random.shuffle(nakupovalni_vozicek)


# =========================
# KONČNI IZPIS
# =========================

# Spremenimo seznam v lepši tekst
vozicek = ", ".join(nakupovalni_vozicek)

# Izpišemo končni nakupovalni voziček
print(f"Vaša košarica presenečenja danes je: {vozicek}.")