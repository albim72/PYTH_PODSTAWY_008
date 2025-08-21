def analizuj_plik(plik_we,plik_wy):
    #odczyt pliku
    with open(plik_we,"r",encoding="utf-8") as f:
        linie = f.readlines()

    #usunięcie znaku nowej linii
    linie = [linia.strip() for linia in linie]

    #przygotowanie danych
    pierwsza = linie[0]
    ostatnia = linie[-1]
    liczba = len(linie)

    #zapis do nowego pliku
    with open(plik_wy,"w",encoding="utf-8") as f:
        f.write(f"Pierwsza linia: {pierwsza}\n")
        f.write(f"Ostatnia linia: {ostatnia}\n")
        f.write(f"Liczba linii: {liczba}\n")

    print(f"Zapisano do pliku: {plik_wy}")

analizuj_plik("dane.txt","wyniki.txt")
