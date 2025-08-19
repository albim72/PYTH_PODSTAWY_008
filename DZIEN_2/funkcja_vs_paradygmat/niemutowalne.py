imiona = ["Anna","Alicja","Bartek","Andrzej","Karol","Agnieszka"]

wynik = len(
    list(
        map(lambda x:x.upper(),
            filter(lambda x:x.startswith("A"), imiona))
    )
)
#funkcja filter wybiera z listy imiona zaczynające się na A
#funkcja map - powiększa litery
#funkcja list towrzy nową listę
#funkcja len zlicza elementy tej nowej listy
print(f"funkcyjnie - liczba imion: {wynik}")
