class KontoBankowe:
    def __init__(self,wlasciciel: str, saldo: float = 0.0):
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    @property
    def wlasciciel(self) -> str:
        """właściciel konta (tylko do odczytu) -> getter"""
        return self._wlasciciel

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self,kwota: float):
        """setter z walidacją"""
        if kwota < 0:
            raise ValueError("Saldo nie może byc ujemne!")
        self._saldo = kwota

    @saldo.deleter
    def saldo(self):
        """deleter - usnięcie salda (wyzerowania) """
        print("saldo zostało wyzerowane!")
        self._saldo = 0.0
        # del self._saldo


#użycie properites

k = KontoBankowe("Jakub",5000)
print(k.wlasciciel)
print(k.saldo)

#nowa kwota saldo
k.saldo = 10000
print(k.saldo)

try:
    k.saldo = -1000
except ValueError as e:
    print(e)

#użycie deletera
del k.saldo
print(k.saldo)

# del k
# print(k)
