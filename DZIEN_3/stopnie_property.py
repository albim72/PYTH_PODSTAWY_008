class Ceslsius:
    def __init__(self, temp_c: float):
        self._temp_c = temp_c

    @property
    def fahrenheit(self) -> float:
        return self._temp_c * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, temp_f: float):
        self._temp_c = (temp_f - 32) * 5 / 9


t = Ceslsius(23)
print(t.fahrenheit)
t.fahrenheit = 211
print(t._temp_c) 
