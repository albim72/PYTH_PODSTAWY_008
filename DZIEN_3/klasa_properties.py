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
