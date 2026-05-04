import random
print(r"""
__        __   _                          _ 
 \ \      / /__| | ___ ___  _ __ ___   ___| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)

        NAKLJUČNA ORODJA

""")

rocno_orodje = ["kladivo", "izvijac", "klesce", "zaga", "meter", "olfa noz", "pile", "imbus kljuc", "francoski kljuc", "vodna tehtnica"]

elektricno_orodje = ["vrtalnik", "kotna brusilka", "vbodna zaga", "krozna zaga", "brusilnik", "akumulatorski vijacnik", "udarni vrtalnik", "rezkar", "spajkalnik", "pistola za vroce lepilo"]

vrtno_orodje = ["lopata", "grablje", "motika", "skarje za zivo mejo", "vrtne skarje", "zalivalka", "samokolnica", "kosilnica", "sekira", "cepilnik"]

merilno_orodje = ["meter", "ravnilo", "kotomer", "subler", "multimeter", "laser meter", "vodna tehtnica", "termometer", "tehtnica", "merilni trak"]

print("Dobrodošli v naključni izbiri orodja")

skatla_za_orodje = []

st_rocno_orodje = int(input("Vnesite kolicino rocnega orodja: "))
st_elektricno_orodje = int(input("Unesite kolicino rocnega orodja: "))
st_vrtno_orodje = int(input("Unesite kolicino rocnega orodja: "))
st_merilno_orodje = int(input("Unesite kolicino rocnega orodja: "))

while len(skatla_za_orodje) < st_rocno_orodje:
    nakljucna_skatla = random.choice(rocno_orodje)
    if rocno_orodje not in skatla_za_orodje:
        skatla_za_orodje.append(nakljucna_skatla)

while len(skatla_za_orodje) < st_rocno_orodje + st_elektricno_orodje:
    nakljucna_skatla = random.choice(elektricno_orodje)
    if elektricno_orodje not in skatla_za_orodje:
        skatla_za_orodje.append(nakljucna_skatla)

while len(skatla_za_orodje) < st_rocno_orodje + st_elektricno_orodje + st_vrtno_orodje:
    nakljucna_skatla = random.choice(merilno_orodje)
    if vrtno_orodje not in skatla_za_orodje:
        skatla_za_orodje.append(nakljucna_skatla)

while len(skatla_za_orodje) < st_rocno_orodje + st_elektricno_orodje + st_vrtno_orodje + st_merilno_orodje:
    nakljucna_skatla = random.choice(vrtno_orodje)
    if merilno_orodje not in skatla_za_orodje:
        skatla_za_orodje.append(nakljucna_skatla)

premesana_skatla = ", ".join(skatla_za_orodje)
print(f"Vaša končna naključna skatla za orodje je: {premesana_skatla}")