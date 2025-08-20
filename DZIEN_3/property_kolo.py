#property jako atrybut wyliczany dynamicznie
import math

class Kolo:
    def __init__(self, r: float):
        self._r = r

    @property
    def pole(self) -> float:
        return math.pi * self._r ** 2

    @property
    def obwod(self) -> float:
        return 2 * math.pi * self._r

kl = Kolo(3.7)
print(f"pole koła: {kl.pole:.3f}")
print(f"obwód koła: {kl.obwod:.3f}")
