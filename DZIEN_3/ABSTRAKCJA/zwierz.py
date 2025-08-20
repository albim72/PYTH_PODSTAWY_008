from abc import ABC, abstractmethod

class Zwierze(ABC):
    def __init__(self,name):
        self._name = name
        self.createnew_animal(self._name)

    @abstractmethod
    def daj_glos(self):
        pass

    @abstractmethod
    def liczba_nog(self):
        return 4

    def createnew_animal(self,name):
        return f"utworzono nowy obiekt {name} klasy Zwierze"


class Pies(Zwierze):
    def __init__(self,name):
        super().__init__(name)

    def daj_glos(self):
        return "Hau!Hau!"

    def liczba_nog(self):
        return super().liczba_nog()


print("_______ Pies _________")
p = Pies("Ludvik")
print(p)
print(p.daj_glos())
print(p.liczba_nog())




