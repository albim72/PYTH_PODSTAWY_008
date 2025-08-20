from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass
    
    @abstractmethod
    def obwod(self):
        pass
    
    
class Prostokat(Figura):
    def __init__(self, bok1, bok2):
        self.bok1 = bok1
        self.bok2 = bok2
        
    def pole(self):
        return self.bok1 * self.bok2
    
    def obwod(self):
        return 2 * (self.bok1 + self.bok2)
    
class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien
        
    def pole(self):
        return math.pi*self.promien ** 2
    
    def obwod(self):
        return 2 * math.pi * self.promien
