from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    name: str
    quantity: int
    price: float

class ShoppingList:
    def __init__(self) -> None:
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def total_cost(self) -> float:
        return sum(i.quantity * i.price for i in self.items)

    def export_txt(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            for i in self.items:
                f.write(f"{i.name} | ilość: {i.quantity} | cena: {i.price:.2f} zł | razem: {i.quantity * i.price:.2f} zł\n")
            f.write(f"\nSUMA: {self.total_cost():.2f} zł\n")

def main() -> None:
    shopping = ShoppingList()

    # przykładowe produkty
    shopping.add_item(Item("Chleb", 2, 4.57))
    shopping.add_item(Item("Mleko", 1, 4.25))
    shopping.add_item(Item("Masło", 4, 7.88))
    shopping.add_item(Item("Twaróg", 2, 6.54))

    # zapis do pliku
    shopping.export_txt("shopping.txt")

    # wydruk w konsoli
    print(f"Suma zakupów: {shopping.total_cost():.2f} zł")

if __name__ == "__main__":
    main()
