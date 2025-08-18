#stówrzmy listę
from statistics import stdev

studenci = ["Ala","Bartek","Leon","Lidia","Marek","Ewa","Ala"]
oceny = [5,5,3,3,2,3,5]

print(studenci)
print(oceny)
print(len(studenci))
print(type(studenci))

# CTRL + / -> komentowanie/odkomentowanie bloku tekstu - kodu
# CTRL + D -> duplikacja bloku

print(studenci[0])
print(studenci[3])
print(studenci[-1])
print(studenci[2:5])
print(studenci[2:])
print(studenci[:6])
print(studenci[:])
print(studenci[:len(studenci)])

#dodawanie elementów
studenci.append("Marcel")
print(studenci)

#wstawianie w konkrentne miejsce
studenci.insert(4,"Ofelia")
print(studenci)

#usuwanie elementów
# studenci.remove("Ala")
# print(studenci)

while "Ala" in studenci:
    studenci.remove("Ala")

print(studenci)

if "Olaf" in studenci:
    studenci.remove("Olaf")
else:
    print("Nie ma Olafa")

#usuwanie po indeksie
del studenci[2]
print(studenci)

usuniety = studenci.pop(3)
print(studenci)
print(usuniety)



