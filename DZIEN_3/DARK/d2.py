class Samozjadacz:
    def __init__(self):
        self.x = 42
        self.y = "sekret"

    def __getattribute__(self, name):
        # Uwaga: używamy object.__getattribute__, inaczej nieskończona rekurencja
        val = object.__getattribute__(self, name)
        # Efekt „pojedz atrybut”: po każdym odczycie usuń go z obiektu
        # (nie rób tego dla metod specjalnych, żeby nie bricknąć od razu)
        if not name.startswith("__") and hasattr(self, "__dict__") and name in self.__dict__:
            del self.__dict__[name]
        return val

s = Samozjadacz()
print(s.x)      # 42 (i x zniknął)
print(s.x)      # AttributeError
print(s.y)      # "sekret" (i y zniknął)
