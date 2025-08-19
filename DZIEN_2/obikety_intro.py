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
