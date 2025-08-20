def czy_palindrom(slowo: str) -> bool:
    """
    Zwraca True, jeśli napis jest palindromem (ignoruje wielkość liter).
    Przykłady:
        czy_palindrom("kajak") -> True
        czy_palindrom("python") -> False
        czy_palindrom("Anna") -> True
    """
    s = slowo.casefold()  # lepsze niż .lower() dla porównań niezależnych od języka
    return s == s[::-1]


class BankAccount:
    """
    Proste konto bankowe z metodami:
      - deposit(amount): wpłata
      - withdraw(amount): wypłata (komunikuje 'Za mało środków!' przy braku środków)
      - __str__: 'Konto właściciela: Jan, saldo: 1500'
    """
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Kwota wpłaty musi być dodatnia.")
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount < 0:
            raise ValueError("Kwota wypłaty musi być dodatnia.")
        if amount > self.balance:
            print("Za mało środków!")
            return False
        self.balance -= amount
        return True

    def __str__(self) -> str:
        # format :g usuwa zbędne '.0' przy liczbach całkowitych
        return f"Konto właściciela: {self.owner}, saldo: {self.balance:g}"


if __name__ == "__main__":
    # Testy z treści zadania
    print(czy_palindrom("kajak"))    # True
    print(czy_palindrom("python"))   # False
    print(czy_palindrom("Anna"))     # True

    konto = BankAccount("Jan", 1000)
    konto.deposit(500)
    print(konto)             # Konto właściciela: Jan, saldo: 1500
    konto.withdraw(2000)     # Za mało środków!
    print(konto)             # Konto właściciela: Jan, saldo: 1500
