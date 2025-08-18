liczby = (5,7,3,23,6,8,56,45,8,86,4,76,98)
print(liczby)
print(type(liczby))

print(liczby[0])
print(liczby.index(8))
#przykład zastosowania
#lista rezerwacji (rząd, miejsce)
rezerwacje = [(1,5),(2,4),(3,7),(11,9)]

print(rezerwacje)
# sprawdzenie dostepności miejsca
miejsce = (2,4)
if miejsce in rezerwacje:
    print(f"miejsce {miejsce} jest zarezerwowane")
else:
    print(f"miejsce {miejsce} jest dostepne")
