def cislo_text(n):
    jednotky = [
        "nula", "jedna", "dva", "tři", "čtyři",
        "pět", "šest", "sedm", "osm", "devět"
    ]
    teens = {
        10: "deset", 11: "jedenáct", 12: "dvanáct",
        13: "třináct", 14: "čtrnáct", 15: "patnáct",
        16: "šestnáct", 17: "sedmnáct",
        18: "osmnáct", 19: "devatenáct"
    }
    desitky = {
        20: "dvacet", 30: "třicet", 40: "čtyřicet",
        50: "padesát", 60: "šedesát", 70: "sedmdesát",
        80: "osmdesát", 90: "devadesát"
    }
    if n < 10:
        return jednotky[n]
    if n < 20:
        return teens[n]
    if n == 100:
        return "sto"
    desitka = (n // 10) * 10
    jednotka = n % 10
    if jednotka == 0:
        return desitky[desitka]
    return desitky[desitka] + " " + jednotky[jednotka]


if __name__ == "__main__":
    try:
        cislo = int(input("Zadej číslo: "))
        if 0 <= cislo <= 100:
            print(cislo_text(cislo))
        else:
            print("Zadej číslo od 0 do 100!")
    except ValueError:
        print("Musíš zadat celé číslo!")
