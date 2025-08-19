#definicja najprostszej klasy
class Samochod:
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model

auto = Samochod("BMW","5")
print(auto.marka)
print(auto.model)
