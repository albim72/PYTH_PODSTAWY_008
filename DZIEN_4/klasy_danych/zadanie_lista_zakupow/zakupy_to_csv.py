import csv
from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    name: str
    quantity: int
    price: float

#napisz funkje - jedna -> towrząca plik csv i zapisująca do niego dane
#druga -> ładująca dane z plik csv

def save_to_csv(items: List[Item], path: str) -> None:
    with open(path, "w", newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "quantity", "price"])
        for item in items:
            writer.writerow([item.name, item.quantity, item.price])

def load_from_csv(path: str) -> List[Item]:
    items: List[Item] = []
    with open(path, "r",newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(Item(
                name = row["name"],
                quantity = int(row["quantity"]),
                price = float(row["price"])
            ))
    return items

def main() -> None:
    shopping = [
        Item("Chleb", 2, 4.57),
        Item("Jajko", 4, 11.90),
        Item("Ser zółty", 2, 8.99),
        Item("Sałata", 1, 7.33),
    ]

    #zapis
    save_to_csv(shopping,"shopping.csv")
    print("Zapisano do pliku shopping.csv")

    #odczyt
    loaded = load_from_csv("shopping.csv")
    print("wczytano z pliku shopping.csv")
    for item in loaded:
        print(item)


if __name__ == '__main__':
    main()

