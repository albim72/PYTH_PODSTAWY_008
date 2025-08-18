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

#konwersja tuple -> list
nb = [41,55,66]
liczby = list(liczby)
liczby.extend(nb)
liczby = tuple(liczby)
print(liczby)

#analiza zmiennej tekstowej
s = "lajkonik"
print(s)
print(s[1])
print(s[4])
print(s[1:5])
print(s[-1])
print(s[::-1])

print(liczby)

print(liczby[2:9:2])
print(liczby[-2:-9:-2])

slaj = list(s)
print(slaj)

slaj.append("i")

print(slaj)

s = str(slaj)
print(s) #str nie łączy elementów listy - wpływa na kazdy element osobno

sk = "".join(slaj)
print(sk)
