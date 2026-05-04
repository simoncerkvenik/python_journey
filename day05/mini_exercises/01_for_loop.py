import random
print(r"""
__        __   _                          _ 
 \ \      / /__| | ___ ___  _ __ ___   ___| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)

        ŽIVILA PRESENEČENJA

""")

sadje = [
    "jabolko",
    "banana",
    "pomaranca",
    "jagoda",
    "grozdje",
    "kivi",
    "ananas",
    "breskev",
    "hruska",
    "limona"
]

zelenjava = [
    "korenje",
    "krompir",
    "paradiznik",
    "kumara",
    "solata",
    "paprika",
    "čebula",
    "brokoli",
    "cvetača",
    "bučka"
]

meso = [
    "piščanec",
    "govedina",
    "svinjina",
    "puran",
    "jagnjetina",
    "raca",
    "slanina",
    "klobasa",
    "pršut",
    "čevapčiči"
]

sladkarije = [
    "čokolada",
    "bonboni",
    "lizika",
    "piškoti",
    "torta",
    "sladoled",
    "krofi",
    "vaflji",
    "muffin",
    "karamela"
]

nakupovalni_vozicek = []

nm_sadje = int(input("Koliko naključnega sadja bi želeli: "))
nm_zelenjava = int(input("Koliko naključne zelenjave bi želeli: "))
nm_meso = int(input("Koliko naključnega mesa bi želeli: "))
nm_sladkarije = int(input("Koliko bi danes cukra naključnega želeli: "))

#for nakup in range(nm_sadje):
 #   nakljucni_nakup = random.choice(sadje)
  #  nakupovalni_vozicek.append(nakljucni_nakup)
while len(nakupovalni_vozicek) < nm_sadje:
    nakljucni_nakup = random.choice(sadje)

    if nakljucni_nakup not in nakupovalni_vozicek:
        nakupovalni_vozicek.append(nakljucni_nakup)

while len(nakupovalni_vozicek) < nm_sadje + nm_zelenjava:
    nakljucni_nakup = random.choice(zelenjava)

    if nakljucni_nakup not in nakupovalni_vozicek:
        nakupovalni_vozicek.append(nakljucni_nakup)

while len(nakupovalni_vozicek) < nm_sadje + nm_zelenjava + nm_meso:
    nakljucni_nakup = random.choice(meso)

    if nakljucni_nakup not in nakupovalni_vozicek:
        nakupovalni_vozicek.append(nakljucni_nakup)

while len(nakupovalni_vozicek) < nm_sadje + nm_zelenjava + nm_meso + nm_sladkarije:
    nakljucni_nakup = random.choice(sladkarije)

    if nakljucni_nakup not in nakupovalni_vozicek:
        nakupovalni_vozicek.append(nakljucni_nakup)


# for nakup in range(nm_zelenjava):
#     nakljucni_nakup = random.choice(zelenjava)
#     nakupovalni_vozicek.append(nakljucni_nakup)
# for nakup in range(nm_meso):
#     nakljucni_nakup = random.choice(meso)
#     nakupovalni_vozicek.append(nakljucni_nakup)
# for nakup in range(nm_sladkarije):
#     nakljucni_nakup = random.choice(sladkarije)
#     nakupovalni_vozicek.append(nakljucni_nakup)

random.shuffle(nakupovalni_vozicek)

vozicek = ", ".join(nakupovalni_vozicek)


print(f"Vaša košarica presenečenja danes je: {vozicek}.")
