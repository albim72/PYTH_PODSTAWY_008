# --- 1) Lista zamówień jako lista krotek (klient, produkt) ---
zamowienia = [
    ("Ala", "kawa"),
    ("Bartek", "herbata"),
    ("Ala", "ciastko"),
    ("Celina", "kawa"),
    ("Bartek", "kawa"),
    ("Darek", "lemoniada"),
]

# --- 2) Wyświetlenie wszystkich zamówień w pętli for ---
print("Wszystkie zamówienia:")
for klient, produkt in zamowienia:
    # prosta odmiana czasownika „zamówił/a” (wersja neutralna bez odmiany)
    print(f"{klient} zamówił(a) {produkt}")
print()

# --- 3) Zbiór unikalnych klientów ---
unikalni_klienci = set([klient for klient, _ in zamowienia])
print("Unikalni klienci:", unikalni_klienci)

# --- 4) Liczba różnych klientów ---
liczba_klientow = len(unikalni_klienci)
print("Liczba różnych klientów:", liczba_klientow)

# --- 5) Lista wszystkich produktów i unikalne produkty ---
wszystkie_produkty = [produkt for _, produkt in zamowienia]
unikalne_produkty = set(wszystkie_produkty)

print("Wszystkie produkty (z duplikatami):", wszystkie_produkty)
print("Unikalne produkty:", unikalne_produkty)

# Dodatkowo: małe podsumowanie
print("\nPodsumowanie:")
print(f"- Zamówień łącznie: {len(zamowienia)}")
print(f"- Różnych klientów: {len(unikalni_klienci)}")
print(f"- Różnych produktów: {len(unikalne_produkty)}")
