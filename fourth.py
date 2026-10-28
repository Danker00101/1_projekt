def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    
    :param figurka: Slovník s klíči 'typ' a 'pozice' (např. {"typ": "král", "pozice": (4, 4)})
    :param cilova_pozice: N-tice (řádek, sloupec)
    :param obsazene_pozice: Množina obsazených pozic
    :return: True, pokud je tah možný, jinak False
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]
    
    radek, sloupec = cilova_pozice
    
    # 1. KROK: Je cílová pozice na šachovnici? (řádky i sloupce 1 až 8)
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False
    
    # 2. KROK: Je cílová pozice volná?
    if cilova_pozice in obsazene_pozice:
        return False
    
    # 3. KROK: Pohyb podle typu figury
    delta_radek = abs(radek - aktualni_pozice[0])
    delta_sloupec = abs(sloupec - aktualni_pozice[1])
    
    if typ == "král":
        # Král se může pohnout maximálně o 1 pole v jakémkoliv směru
        # (nesmí zůstat na stejném místě)
        return delta_radek <= 1 and delta_sloupec <= 1 and (delta_radek + delta_sloupec) >= 1
        
    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru L (2 a 1, nebo 1 a 2)
        return (delta_radek == 2 and delta_sloupec == 1) or (delta_radek == 1 and delta_sloupec == 2)
    
    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 nahoru, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # False (není L-tvar)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)
