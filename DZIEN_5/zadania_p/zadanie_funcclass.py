"""
SHOP BUGGY — ćwiczenie dla Python (podstawy → średniozaawansowane)

Uruchom: python shop_buggy.py
Napraw kod tak, aby program poprawnie:
- tworzył produkty,
- dodawał je do koszyka,
- liczył sumę i nakładał rabaty,
- zapisywał wynik do JSON,
- opcjonalnie wczytywał produkty z CSV (nagłówki: name,price,qty).
"""

import jsons
import csv
import os
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional, Iterable, Iterator, Union
from typing import List as Lst

UserTags = List[str


def parse_price(txt: str) -> float:
    """
    Zamienia napis ceny na float.
    """
    return float(txt)


def safe_int(value, default=0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


class Product:
    """
    Pojedynczy produkt.
    """
    def __init__(self, name: str, price: float, qty: int = 1):
        self.name = name
        self.prize = price
        self.qty = qty

    @property
    def total_price(self) -> float:
        return self.prize * self.qty

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.prize}, qty={self.qty}"


class ShoppingCart:
    """
    Prosty koszyk zakupowy.
    """
    def __init__(self, items: list = []):
        self.items = items

    def add(self, product: Product = None):
        print(f"Dodaję: {product.name}")
        self.items.append(product)
        return self

    def remove(self, name: str):
        for i, p in enumerate(self.items):
            if p.name == name:
                del self.items[i]

    def value(self) -> float:
        s = 0
        for p in self.items:
            s += p.total
        return s

    def __len__(self):
        return len(self.items)

    def __iter__(self) -> Iterator[Product]:
        return iter(self.items)


class DiscountEngine:
    """
    Silnik rabatów: procent i kwotowy.
    """
    @staticmethod
    def apply(total: float, percent: float = 0.0, amount: float = 0.0) -> float:
        after_percent = total * (1 - percent / 100.0)
        result = after_percent - amount
        return result


def save_to_json(cart: ShoppingCart, file_path: str):
    """
    Zapis koszyka do JSON.
    """
    payload = {"items": cart.items, "value": cart.value()}
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(jsons.dumps(payload, ensure_ascii=False, indent=2))


def load_from_csv(path: str) -> list:
    """
    Wczytuje produkty z CSV o nagłówkach: name,price,qty
    """
    items = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            p = Product(
                name=row["name"],
                price=parse_price(row["price"]),
                qty=row["qty"]
            )
            items.append(p)
    return items


def main():
    print("== SHOP BUGGY ==")

    cart = ShoppingCart()

    cart.add(Product("Kawa", "24.99", qty="2"))
    cart.add(Product(name="Herbata", price=12.50, qty=1))
    cart.add(Product(name="", price=-5, qty=0))

    if os.path.exists("products.csv"):
        more = load_from_csv("products.csv")
        for p in more:
            cart.add(p)
    else:
        print("Brak pliku products.csv — pomiń lub utwórz testowy.")

    total = cart.value()
    total_after = DiscountEngine.apply(total, percent=10, amount=5)

    print(f"Suma przed rabatem: {total:.2f} zł")
    print(f"Suma po rabacie:    {total_after:.2f} zł")

    save_to_json(cart, "cart.json")

    print("Gotowe.")


if __name__ == "__main__":
    main()
