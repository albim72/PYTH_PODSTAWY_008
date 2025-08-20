while True:
    try:
        #kod który może wywołac wyjątek
        tekst = input("Podaj liczbę albo wpisz exit żeby zakończyc program: ")
        if tekst.lower() == "exit":
            print("koniec działania programu")
            break
        liczba = int(tekst)
        wynik = 10 / liczba
    except ValueError:
        print("To nie jest poprawna liczba!")
    except ZeroDivisionError:
        print("Nie dziel przez zero!")
    else:
        print(f"Wynik dzielenia: {wynik}")
    finally:
        print("Liczymy dalej...")
