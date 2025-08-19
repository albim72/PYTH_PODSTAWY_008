"""
Rozwiązanie zadania: „System zarządzania klasą” — kolekcje w Pythonie
"""

from statistics import mean
from datetime import datetime

# ===== 1. LISTA (list) =====
print("=== [1] Lista uczniów ===")
uczniowie = ["Ala", "Bartek", "Celina"]
print("Start:", uczniowie)

uczniowie.append("Darek")
uczniowie.extend(["Ewa", "Franek"])
print("Po dodaniu:", uczniowie)

uczniowie.remove("Celina")
print("Po usunięciu 'Celina':", uczniowie)

print("Lista z numeracją:")
for i, imie in enumerate(uczniowie, start=1):
    print(f"{i}. {imie}")
print()

# ===== 2. KROTKA (tuple) =====
print("=== [2] Krotka ucznia ===")
uczen = ("Ala", "Kowalska", 2010)
print("Uczeń:", uczen)
print("Rok urodzenia:", uczen[2])

try:
    uczen[2] = 2011
except TypeError as e:
    print("Próba zmiany roku w krotce:", repr(e))
print()

# ===== 3. ZBIORY (set / frozenset) =====
print("=== [3] Zbiory — koło matematyczne i sportowe ===")
kolo_matematyczne = {"Ala", "Bartek", "Ewa"}
kolo_sportowe = {"Bartek", "Celina", "Ewa", "Franek"}
print("Matematyczne:", kolo_matematyczne)
print("Sportowe    :", kolo_sportowe)

oba = kolo_matematyczne & kolo_sportowe
tylko_sport = kolo_sportowe - kolo_matematyczne
unikalni = kolo_matematyczne | kolo_sportowe
print("Chodzą na oba koła (∩):", oba)
print("Chodzą tylko na sportowe (A\\B):", tylko_sport)
print("Wszyscy unikalni (∪):", unikalni)

kolo_matematyczne_fs = frozenset(kolo_matematyczne)
print("frozenset(matematyczne):", kolo_matematyczne_fs)
try:
    kolo_matematyczne_fs.add("Gosia")
except AttributeError as e:
    print("Próba dodania do frozenset:", repr(e))
print()

# ===== 4. SŁOWNIK (dict) =====
print("=== [4] Słownik ocen ===")
oceny = {
    "Ala": [5, 4, 3],
    "Bartek": [3, 3, 4],
    "Celina": [6, 5]
}
print("Start:", oceny)

oceny["Darek"] = [4, 4, 5]
print("Po dodaniu Darka:", oceny)

oceny.setdefault("Ala", []).append(5)
print("Po dopisaniu oceny Ali:", oceny)

print("Średnie ocen:")
for uczen, lista in oceny.items():
    sr = mean(lista) if lista else float("nan")
    print(f"{uczen} → {sr:.1f}")
print()

# ===== Zadanie dodatkowe =====
print("=== [Zadanie dodatkowe] Słownik z danymi i średni wiek ===")
uczniowie_info = {
    "Ala": ("Kowalska", 2010),
    "Bartek": ("Nowak", 2009),
    "Celina": ("Wiśniewska", 2011),
    "Darek": ("Zieliński", 2008),
    "Ewa": ("Lewandowska", 2010),
    "Franek": ("Kamiński", 2009),
}

rok_biezacy = datetime.now().year
wieks = [rok_biezacy - rok for (_nazwisko, rok) in uczniowie_info.values()]
sredni_wiek = mean(wieks) if wieks else float("nan")

for imie, (nazwisko, rok) in uczniowie_info.items():
    wiek = rok_biezacy - rok
    print(f"{imie} {nazwisko} — ur. {rok}, wiek: {wiek}")

print(f"Średni wiek grupy: {sredni_wiek:.2f} roku")
