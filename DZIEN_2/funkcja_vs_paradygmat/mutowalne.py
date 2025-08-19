
imiona = ["Anna","Alicja","Bartek","Andrzej","Karol","Agnieszka"]
def znajdz_i_zmien(imiona):
    wynik = []
    for imie in imiona:
        if imie.startswith('A'):
            wynik.append(imie.upper())
    return wynik


wynik = znajdz_i_zmien(imiona)
print(len(wynik))

print(imiona)

print(len(znajdz_i_zmien(imiona)))
print(imiona)
print(wynik)

print("______ przypadek modyfikacji globalnej ______")
wynik = []
def znajdz_i_zmien(imiona):
    for imie in imiona:
        if imie.startswith('A'):
            wynik.append(imie.upper())

znajdz_i_zmien(imiona)
print(len(wynik))
print(imiona)
print(wynik)

