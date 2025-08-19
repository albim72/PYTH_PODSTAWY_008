#definicja najprostszej klasy
class Samochod:
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model

auto = Samochod("BMW","5")
print(auto.marka)
print(auto.model)

#metoda w klasie
class Prostokat:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def pole(self):
        return self.a*self.b

p = Prostokat(5,3)
print(f"pole prostokąta to: {p.pole()}")

#dziedziczenie

class Zwierze:
    def __init__(self,imie):
        self.imie=imie

    def dzwiek(self):
        return "???"

class Pies(Zwierze):
    def __init__(self,imie,rasa):
        super().__init__(imie)
        self.rasa=rasa

    def dzwiek(self):
        return "Hau!"


class Kot(Zwierze):
    def __init__(self, imie, umaszczenie):
        super().__init__(imie)
        self.umaszczenie=umaszczenie

    def dzwiek(self):
        return "Miau!"

pies = Pies("Ludvik", "Bulfog Angielski")
print(f"dzwiek psa to: {pies.dzwiek()}")

kot = Kot("Ator","rude")
print(f"dzwiek kota to: {kot.dzwiek()}")

pies = Pies("Roman", "Owczarek Belgijski")
print(f"dzwiek psa to: {pies.dzwiek()}")



