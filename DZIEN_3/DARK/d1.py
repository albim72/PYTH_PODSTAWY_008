class Pies:
    def glos(self): return "hau"
    def __repr__(self): return "<Pies>"

class Kot:
    def glos(self): return "miau"
    def __repr__(self): return "<Kot>"

class Zwierze:
    def __init__(self, gatunek):
        # „Spektakl”: zmień klasę instancji po inicjalizacji
        if gatunek == "pies":
            self.__class__ = Pies
        elif gatunek == "kot":
            self.__class__ = Kot
        else:
            raise ValueError("nieznany gatunek")

z = Zwierze("pies")
print(z, z.glos())   # <Pies> hau

# Ten sam konstruktor może stworzyć „to samo” jako inny typ:
w = Zwierze("kot")
print(w, w.glos())   # <Kot> miau
