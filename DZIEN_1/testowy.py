print("Witaj w świecie Pythona!")

x = 5
y = 7
print(x + y)


def multiply(zmienna_a, zmienna_b):
    return zmienna_a * zmienna_b


print(multiply(x, y))

#zmienne i typy
x:float = 8.82
print(x)
print(type(x))

x:str = "osiem"
print(x)
print(type(x))

_r_ = 0.45 #zmienna typu protected  chroniona -> pokreslnik z przodu
#podkreslnik z tyłu nadaj mu symboliczną rolę - np. zmiennej specjalnej
print(_r_)
print(type(_r_))

__info = "info" #zmienna typu private prywatna
print(__info)
print(type(__info))

#uwaga nazwy zrezerwowane! __init__, __str__.....

# __init__ = "taakie tam"
# print(__init__)
# print(type(__init__))

#może Python nie zablkuje ale problm z OOP  obiektowe

u = "3.8"
print(u*9)

# print(int(u)*9)
print(eval(u)*9)


