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

#iteracja po liście
for ind,var in enumerate(studenci): #enumerate zwraca parę (indeks,wartośc)
    print(f"Indeks {ind+1} - {var}") #f-string - ekstrapolacja tekstu

#łączenie list
nowi = ["Hubert","Iza"]
studenci.extend(nowi)
print(studenci)

kolejni = ["Justyna","Ula","ula"]
studenci = studenci + kolejni
print(studenci)

#list comprehension
print("____ list comprehension _____")
kwadraty = [x**2 for x in range(1,13)]
print(kwadraty)

oceny_pow_3 = [o for o in oceny if o>3]
print(oceny_pow_3)

#sortowanie elementów
print("______SORTOWANIE______")
print(f"studenci alfabetycznie:{sorted(studenci)}")
print(f"studenci sortowani odwrotnie: {sorted(studenci,reverse=True)}")

#listy złożone

print("______listy wielowymiarowe______")
tabela = [
    ["Ala",5],
    ["Olaf",3],
    ["Karol",4],
    ["Maria",5],
    ["Ela",3]
]

for imie,ocena in tabela:
    print(f"{imie} ma ocenę {ocena}")

print("____funkcje ageregujące na listach____")
print(f"ocena najwyższa: {max(oceny)}")
print(f"ocena najniższa: {min(oceny)}")
print(f"srednia oceny: {sum(oceny)/len(oceny)}")
print(f"odchylenie standardowe: {stdev(oceny)}")





