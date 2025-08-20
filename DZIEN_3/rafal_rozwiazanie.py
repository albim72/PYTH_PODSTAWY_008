# Zadanie 1

def czy_palindrom(slowo):
    if type(slowo) == str:
        slowo = slowo.lower()   # .casefold() jet lepsze ze względu na języki
        slowo2 = ""
        for i in range(1,len(slowo)+1):
            slowo2 = slowo2 + slowo[-i]
        if slowo == slowo2:
            return True
        else:
            return False
    else:
        return "Argument nietekstowy"

word = "Anna"
print(czy_palindrom(word))
print(word)

word = "Rafał"
print(czy_palindrom(word))
print(word)

#Zadanie 2

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def Deposit(self,Amount):
        if Amount<0:
            print("Nie można wpłacić kwoty ujemnej!")
        else:
            self.balance += Amount

    def Withdraw(self,Amount):
        if self.balance >= Amount:
            self.balance -= Amount
        else:
            print(f"Za mało środków!\nMaksymalnie można wypłacić: {self.balance:.2f}.")

    def __str__(self):
        return f"Bank account owner: {self.owner}\nBalance: {self.balance:.2f}"

dane=BankAccount("Anna",1000)
dane.Deposit(500)
dane.Withdraw(200)
dane.Withdraw(400)
print(dane)
