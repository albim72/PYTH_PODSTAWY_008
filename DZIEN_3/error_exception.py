try:
    #kod który może wywołac wyjątek
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba
except ValueError:
    print("To nie jest poprawna liczba!")
except ZeroDivisionError:
    print("Nie dziel przez zero!")
else:
    print(f"Wynik dzielenia: {wynik}")
finally:
    print("Koniec programu!")
