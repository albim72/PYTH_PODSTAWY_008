from typing import List,Iterable

def analizuj_plik(plik_we: str,plik_wy: str,fraza: str) -> None:
    #odczyt pliku i zwrócenie jako lista linii

    def wczytaj_linie(nazwa: str) -> List[str]:
        with open(nazwa,"r",encoding="utf-8") as f:
            return [linia.strip() for linia in f.readlines()]

    #sprawdzenie czy fraza występiuje w zbiorze linii
    def czy_zawiera_fraze(linie: Iterable[str],fraza: str) -> bool:
        return any(fraza.lower() in linia.lower() for linia in linie)

    #główna logika
    linie: List[str] = wczytaj_linie(plik_we)
    pierwsza: str = linie[0]
    ostatnia: str = linie[-1]
    liczba: int = len(linie)
    znaleziono: bool = czy_zawiera_fraze(linie,fraza)

    #zapis do nowego pliku
    with open(plik_wy,"w",encoding="utf-8") as f:
        f.write(f"Pierwsza linia: {pierwsza}\n")
        f.write(f"Ostatnia linia: {ostatnia}\n")
        f.write(f"Liczba linii: {liczba}\n")
        f.write(f"fraza '{fraza}' {'znaleziona' if znaleziono else 'nie znaleziona'}")

    print(f"Zapisano do pliku: {plik_wy}")

analizuj_plik("dane.txt","wyniki.txt", "Java")
