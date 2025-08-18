ksiazki = {
"978-83-240-0010-0": "Pan Tadeusz",
"978-83-240-0744-3": "Lalka",
"978-83-240-1345-3": "Quo Vadis"
}

print(ksiazki)
print(f"książka {ksiazki['978-83-240-0010-0']}")

#dodawanie do słownika
ksiazki["978-83-240-7345-5"] = "Krzyżacy"
print(ksiazki)

#iteracja po słowniku:
print("________ksiażki___________")
for k,v in ksiazki.items():
    print(f"{k} - {v}")

#sprawdzenie klucza

print("\nCzy mamy -> 978-83-240-7345-5 ??","978-83-240-7345-5" in ksiazki)
print("\nCzy mamy -> 978-83-240-7345-5 ??","978-83-240-7885-5" in ksiazki)
