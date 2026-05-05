import random

print(r"""
__        __   _                          _ 
 \ \      / /__| | ___ ___  _ __ ___   ___| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)

        NAKLJUČNA ORODJA

""")

# =========================
# LISTS OF TOOLS
# =========================

# Manual tools
rocno_orodje = [
    "kladivo", "izvijac", "klesce", "zaga", "meter",
    "olfa noz", "pile", "imbus kljuc", "francoski kljuc",
    "vodna tehtnica"
]

# Electric tools
elektricno_orodje = [
    "vrtalnik", "kotna brusilka", "vbodna zaga", "krozna zaga",
    "brusilnik", "akumulatorski vijacnik", "udarni vrtalnik",
    "rezkar", "spajkalnik", "pistola za vroce lepilo"
]

# Garden tools
vrtno_orodje = [
    "lopata", "grablje", "motika", "skarje za zivo mejo",
    "vrtne skarje", "zalivalka", "samokolnica", "kosilnica",
    "sekira", "cepilnik"
]

# Measuring tools
merilno_orodje = [
    "meter", "ravnilo", "kotomer", "subler", "multimeter",
    "laser meter", "vodna tehtnica", "termometer", "tehtnica",
    "merilni trak"
]


# =========================
# USER INPUT
# =========================

print("Dobrodošli v naključni izbiri orodja")

# Empty toolbox
skatla_za_orodje = []

# Ask user how many tools from each category they want
st_rocno_orodje = int(input("Vnesite količino ročnega orodja: "))
st_elektricno_orodje = int(input("Vnesite količino električnega orodja: "))
st_vrtno_orodje = int(input("Vnesite količino vrtnega orodja: "))
st_merilno_orodje = int(input("Vnesite količino merilnega orodja: "))


# =========================
# RANDOM MANUAL TOOLS
# =========================

# Add random manual tools until we have enough of them
while len(skatla_za_orodje) < st_rocno_orodje:
    nakljucna_skatla = random.choice(rocno_orodje)

    # Add tool only if it is not already in the toolbox
    if nakljucna_skatla not in skatla_za_orodje:
        skatla_za_orodje.append(nakljucna_skatla)


# =========================
# RANDOM ELECTRIC TOOLS
# =========================

# Add random electric tools after manual tools
while len(skatla_za_orodje) < st_rocno_orodje + st_elektricno_orodje:
    nakljucna_skatla = random.choice(elektricno_orodje)

    # Add tool only if it is not already in the toolbox
    if nakljucna_skatla not in skatla_za_orodje:
        skatla_za_orodje.append(nakljucna_skatla)


# =========================
# RANDOM GARDEN TOOLS
# =========================

# Add random garden tools after manual and electric tools
while len(skatla_za_orodje) < st_rocno_orodje + st_elektricno_orodje + st_vrtno_orodje:
    nakljucna_skatla = random.choice(vrtno_orodje)

    # Add tool only if it is not already in the toolbox
    if nakljucna_skatla not in skatla_za_orodje:
        skatla_za_orodje.append(nakljucna_skatla)


# =========================
# RANDOM MEASURING TOOLS
# =========================

# Add random measuring tools after all previous tools
while len(skatla_za_orodje) < st_rocno_orodje + st_elektricno_orodje + st_vrtno_orodje + st_merilno_orodje:
    nakljucna_skatla = random.choice(merilno_orodje)

    # Add tool only if it is not already in the toolbox
    if nakljucna_skatla not in skatla_za_orodje:
        skatla_za_orodje.append(nakljucna_skatla)


# =========================
# FINAL OUTPUT
# =========================

# Turn list into one readable string
premesana_skatla = ", ".join(skatla_za_orodje)

# Print final toolbox
print(f"Vaša končna naključna škatla za orodje je: {premesana_skatla}")