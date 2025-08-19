def pole_prostokata(a, b):
    """
    Funkcja oblicza pole prostokąta.
    Argumenty:
        a (float/int): długość pierwszego boku
        b (float/int): długość drugiego boku
    Zwraca:
        float/int: pole prostokąta
        str: komunikat błędu, jeśli dane są niepoprawne
    """
    if a <= 0 or b <= 0:
        return "Boki muszą być dodatnie!"
    return a * b


# --- Przykładowe użycie ---
print(pole_prostokata(5, 3))    # 15
print(pole_prostokata(10, -2))  # "Boki muszą być dodatnie!"
print(pole_prostokata(7, 4))    # 28
print(pole_prostokata(0, 4))
