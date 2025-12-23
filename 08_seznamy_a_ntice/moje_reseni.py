def vytvor_seznam_zvirat():
    return ["andulka", "had", "kočka", "králík", "pes"] # zvirata podle abecedy

def filtruj_kratka_jmena(seznam):
    kratka_jmena = []  # Vytvoření prázdného seznamu pro krátká jména
    for jmeno in seznam:  # Pro každý řetězec v zadaném seznamu
        if len(jmeno) < 5:  # Kontrola délky řetězce
            kratka_jmena.append(jmeno)  # Přidání krátkého jména do nového seznamu
    return kratka_jmena  # Vrácení seznamu krátkých jmen

def filtruj_k(seznam):
    k_jmena = []  # Vytvoření prázdného seznamu pro jména začínající na 'k'
    for jmeno in seznam:  # Pro každý řetězec v zadaném seznamu
        if jmeno.startswith('k'):  # Kontrola, zda řetězec začíná na 'k'
            k_jmena.append(jmeno)  # Přidání jména do nového seznamu
    return k_jmena  # Vrácení seznamu jmen začínajících na 'k'

def obsahuje(seznam, slovo):
    for prvek in seznam:  # Pro každý prvek v seznamu
        if prvek == slovo:  # Porovnání prvku se zadaným slovem
            return True  # Pokud se shodují, vrátí True
    return False  # Pokud se nenašlo shodné slovo, vrátí False

def bez_prvniho(seznam):
    return seznam[1:]  # Vrátí nový seznam bez prvního prvku

def serad_od_druheho(seznam):
    dvojice = []  # Vytvoření prázdného seznamu pro dvojice (klíč, hodnota)
    for hodnota in seznam:  # Pro každý prvek v zadaném seznamu
        klic = hodnota[1:]  # Vypočítání klíče (hodnota bez prvního znaku)
        dvojice.append((klic, hodnota))  # Přidání dvojice (klíč, hodnota) do seznamu
    dvojice.sort()  # Seřazení seznamu dvojic podle klíče
    serazeny_seznam = []  # Vytvoření prázdného seznamu pro výsledné hodnoty
    for _, hodnota in dvojice:  # Pro každou dvojici v seřazeném seznamu, _ = ignoruj klíč
        serazeny_seznam.append(hodnota)  # Přidání hodnoty do výsledného seznamu
    return serazeny_seznam  # Vrácení seřazeného seznamu hodnot

import random
def vytvor_balicek():
    hodnoty = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    barvy = ['♥', '♦', '♠', '♣']
    balicek = []  # Vytvoření prázdného seznamu pro balíček karet
    for barva in barvy:  # Pro každou barvu
        for hodnota in hodnoty:  # Pro každou hodnotu
            balicek.append((hodnota, barva))  # Přidání dvojice (hodnota, barva) do balíčku
    random.shuffle(balicek)  # Zamíchání balíčku karet
    return balicek  # Vrácení zamíchaného balíčku

