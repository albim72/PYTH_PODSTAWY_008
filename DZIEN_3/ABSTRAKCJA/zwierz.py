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
