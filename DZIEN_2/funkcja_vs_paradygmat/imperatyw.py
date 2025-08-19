#funkcja ma wykonac działanie na liście danych:
# -> znajdź liczby parzyste
# -> podnieś je do kwadratu
# -> zsumuj wyniki

def znajdz_parzyste(lista):
    wynik = []
    for x in lista:
        if x % 2 == 0:
            wynik.append(x)
    return wynik

def podnies_do_kwadratu(lista):
    return [x**2 for x in lista]

def suma(lista):
    wynik = 0
    for x in lista:
        wynik += x  #wynik[nowy] = wynik[stary] + x
    return wynik


liczby = list(range(1,11))
print(liczby)

parzyste = znajdz_parzyste(liczby)
print(parzyste)

kwadraty = podnies_do_kwadratu(parzyste)
print(kwadraty)

suma = suma(kwadraty)
print(suma)


