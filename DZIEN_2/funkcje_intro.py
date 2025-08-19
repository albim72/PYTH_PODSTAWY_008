"""
opiszemy grupę funkcji
pokażemy różne aspekty wykorzystanie funkcji w Pythonie
"""

#prosta funkcja bez argumentów
def powitanie():
    print("Witaj w świecie Pythona!")

#funlcja z jednym argumentem
def kwadrat(x):
    return x**2
#funkcja z dwoma argumentami
def suma(a,b):
    return a+b

#funkcja z wartością domyślną
def powitanie_uzytkownika(imie,jezyk="PL"):
    if jezyk=="PL":
        print(f"Witaj, {imie}!")
    elif jezyk=="EN":
        print(f"Hello, {imie}!")
    else:
        print(f"[{jezyk}] Nieobsługiwany język. Cześc {imie}!")

#funkcja zwracająca wiele wartości
def dzielenie(a,b):
    """
    zwraca (iloraz całkowity,reszta) dla liczb całkowitych a i b
    :param a: int
    :param b: int
    :return: divmod(a,b)
    """
    if b==0:
        raise ZeroDivisionError("Nie dziel przez zero!")
    return divmod(a,b)
#przykładowe użuycia funkcji
if __name__ == '__main__':
    print("_____ funkcja - powitanie_____")
    powitanie()
    print("_____ funkcja - kwadrat_____")
    print(f"kwadrat(7) = {kwadrat(7)}")
    print("_____ funkcja - suma_____")
    print(f"suma(2,3) = {suma(2,3)}")
    print("_____ funkcja - powitanie_uzytkownika_____")
    print(f"powitanie_uzytkownika('Marek') ->")
    powitanie_uzytkownika('Marek')
    print(f"powitanie_uzytkownika('Marek', 'EN') ->")
    powitanie_uzytkownika('Marek', 'EN')
    print(f"powitanie_uzytkownika('Marek', 'DE') ->")
    powitanie_uzytkownika('Marek', 'DE')
    print("_____ funkcja - dzielenie_____")
    iloraz,reszta = dzielenie(17,5)
    print(f"dzielenie(17,5) -> iloraz: {iloraz} ,reszta: {reszta}")
