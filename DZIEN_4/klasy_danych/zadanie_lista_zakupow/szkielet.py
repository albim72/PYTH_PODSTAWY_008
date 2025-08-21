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
        # TODO: dodać przedmiot do listy
        ...

    def total_cost(self) -> float:
        # TODO: policzyć sumę (quantity * price)
        ...

    def export_txt(self, path: str) -> None:
        # TODO: zapisać każdy przedmiot i sumę do pliku
        ...

def main() -> None:
    shopping = ShoppingList()
    # TODO: utworzyć kilka przedmiotów i dodać do listy
    # shopping.add_item(Item("Chleb", 2, 4.50))
    # shopping.add_item(Item("Mleko", 1, 3.20))
    # ...
    # TODO: zapisać do shopping.txt
    # shopping.export_txt("shopping.txt")
    pass

if __name__ == "__main__":
    main()
