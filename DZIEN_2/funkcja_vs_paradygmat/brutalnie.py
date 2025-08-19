# =======================
# PRZYKŁAD 0: globalny kontekst
# =======================
LICZNIK = 0
BUFORY = []
KONFIG = {"tryb": "dev", "retries": 1}

def pokaz_stan(naglowek):
    print(f"\n--- {naglowek} ---")
    print("LICZNIK:", LICZNIK)
    print("BUFORY :", BUFORY)
    print("KONFIG :", KONFIG)

pokaz_stan("START")


# =======================
# 1) Jawna zmiana globali przez 'global'
# =======================
def zly_increment():
    # Rebinding zmiennej globalnej (bez 'global' byłby UnboundLocalError)
    global LICZNIK
    LICZNIK += 1                 # modyfikacja globalnego stanu
    BUFORY.append(LICZNIK)       # mutacja globalnej listy (bez 'global', ale to nadal globalny efekt)
    KONFIG["retries"] += 1       # mutacja globalnego słownika

zly_increment()
zly_increment()
pokaz_stan("PO zly_increment() x2")


# =======================
# 2) Ukryta modyfikacja globalnego stanu przez argument (mutacja in place)
# =======================
def dopisz_brutalnie(lst, x):
    # lst to referencja do globalnej listy BUFORY — mutujemy ją "przez boczne drzwi"
    for _ in range(3):
        lst.append(x)

dopisz_brutalnie(BUFORY, "X")
pokaz_stan("PO dopisz_brutalnie(BUFORY, 'X')")


# =======================
# 3) Mutowalny argument domyślny jako pułapka "pamiętająca stan"
# =======================
def akumulator(wartosc, magazyn=[]):
    # UWAGA: 'magazyn' tworzy się RAZ przy definicji funkcji i żyje globalnie w module
    magazyn.append(wartosc)
    return magazyn

print("\nAkumulator #1:", akumulator(10))
print("Akumulator #2:", akumulator(20))
print("Akumulator #3:", akumulator(30))
# Powyżej każdy kolejny call "pamięta" poprzedni stan — ukryty global przez domyślny mutowalny argument!


# =======================
# 4) Monkey-patching: podmiana globalnej funkcji w locie
# =======================
def strategia():
    return "stara strategia"

def podmien_strategie():
    global strategia
    def nowa():
        return "NOWA strategia (global podmieniony)"
    strategia = nowa  # podmiana referencji globalnej funkcji

print("\nPrzed podmianą:", strategia())
podmien_strategie()
print("Po podmianie  :", strategia())


# =======================
# 5) Efekty uboczne + „logowanie” do globalnej struktury
# =======================
LOGI = []

def wykonaj_operacje(x):
    # „Czysta” matematyka + brudny efekt uboczny (zapis do globalnego logu)
    wynik = x * x
    LOGI.append({"wej": x, "wyj": wynik})
    return wynik

for v in [2, 3, 4]:
    _ = wykonaj_operacje(v)

print("\nLOGI (global):", LOGI)


# =======================
# 6) Warunek wyścigu: „niewinne” ++ na globalu (brutalne w wielowątkowości)
# =======================
import threading, time

KASA = 0
def wplata(n, ile):
    global KASA
    for _ in range(n):
        tmp = KASA          # odczyt globalu
        time.sleep(0.0001)  # okienko na wyścig
        KASA = tmp + ile    # zapis globalu

t1 = threading.Thread(target=wplata, args=(50, 1))
t2 = threading.Thread(target=wplata, args=(50, 1))
t1.start(); t2.start()
t1.join(); t2.join()
print("\nKASA (oczekiwanie=100, realnie może być < 100 przez race condition):", KASA)


# =======================
# 7) Zmiana „konfiguracji” wpływająca globalnie i nieprzewidywalnie
# =======================
def przelacz_tryb(produkcyjny: bool):
    # globalny „feature flag”
    KONFIG["tryb"] = "prod" if produkcyjny else "dev"
    # (potem gdzieś w innym miejscu modułu kod zachowuje się INACZEJ, bo sprawdza KONFIG["tryb"])

przelacz_tryb(True)
pokaz_stan("PO przelacz_tryb(True)")
