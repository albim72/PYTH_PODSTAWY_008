from __future__ import annotations
from typing import (
    TypedDict, Literal, NewType, Protocol, TypeVar, Iterable,
    Mapping, Optional, Callable, overload, Annotated, Generic, Union
)

# --- 1) Modele danych ---

ProductID = NewType("ProductID", int)

class ProductTD(TypedDict):
    id: ProductID
    name: str
    price: Annotated[float, ">=0"]
    category: Literal["book", "food", "electronics"]

class Priced(Protocol):
    price: float

T = TypeVar("T", bound=Priced)

class CartItem(Generic[T]):
    def __init__(self, item: T, qty: int) -> None:
        if qty < 1:
            raise ValueError("qty musi być >= 1")
        self.item = item
        self.qty = qty

    @property
    def line_total(self) -> float:
        return float(self.item.price) * self.qty  # type: ignore[reportAny]

# --- 2) Kalkulacje ---

def subtotal(items: Iterable[CartItem[T]]) -> float:
    return float(sum(ci.line_total for ci in items))

DiscountRule = Callable[[float], float]

def flat_pct(pct: float) -> DiscountRule:
    if not (0.0 <= pct <= 1.0):
        raise ValueError("pct musi być w zakresie [0, 1]")
    def _rule(total: float) -> float:
        return max(0.0, total * (1.0 - pct))
    return _rule

def threshold(threshold: float, drop: float) -> DiscountRule:
    if threshold < 0 or drop < 0:
        raise ValueError("threshold i drop muszą być >= 0")
    def _rule(total: float) -> float:
        return max(0.0, total - drop) if total >= threshold else total
    return _rule

def apply_discount(total: float, rule: DiscountRule) -> float:
    return rule(total)

# --- 3) Walidacja produktu ---

def validate_product(p: ProductTD) -> None:
    if not p["name"].strip():
        raise ValueError("name nie może być puste")
    if p["price"] < 0:
        raise ValueError("price musi być >= 0")
    if p["category"] not in ("book", "food", "electronics"):
        raise ValueError("category spoza dozwolonych Literal[...]")

# --- 4) Overloads dla get_price ---

@overload
def get_price(x: ProductTD) -> float: ...
@overload
def get_price(x: Priced) -> float: ...

def get_price(x):
    # Obsługa ProductTD (TypedDict jest dict-em w runtime):
    if isinstance(x, dict) and "price" in x:
        return float(x["price"])
    # Obsługa dowolnego obiektu spełniającego Protocol Priced
    if hasattr(x, "price"):
        return float(getattr(x, "price"))
    raise TypeError("get_price: nieobsługiwany typ")

# --- 5) Bezpieczne lookup ---

def safe_lookup(
    products: Mapping[ProductID, ProductTD],
    pid: ProductID
) -> Optional[ProductTD]:
    return products.get(pid)

# --- 6) Union i formatowanie ---

def format_money(x: Union[int, float, str]) -> str:
    if isinstance(x, (int, float)):
        return f"{float(x):.2f}"
    # str — prosta walidacja: spróbuj sparsować do float, jeśli się da, sformatuj; jeśli nie, zwróć oryginał
    try:
        val = float(x.replace(",", "."))
        return f"{val:.2f}"
    except ValueError:
        return x  # zostaw bez zmian (świadomie)

# --- Przykładowe użycie/testy ręczne ---

if __name__ == "__main__":
    # Zbuduj kilka produktów (TypedDict)
    prod1: ProductTD = {"id": ProductID(1), "name": "Book A", "price": 49.0, "category": "book"}
    prod2: ProductTD = {"id": ProductID(2), "name": "Headphones", "price": 299.99, "category": "electronics"}
    prod3: ProductTD = {"id": ProductID(3), "name": "Honey", "price": 25.5, "category": "food"}

    # Walidacja
    validate_product(prod1)
    validate_product(prod2)
    validate_product(prod3)

    # Obiekt spełniający Protocol Priced
    class ProductObj:
        def __init__(self, name: str, price: float) -> None:
            self.name = name
            self.price = price

    obj = ProductObj("Premium Cable", 79.9)

    # Koszyk: mieszanka obiektów (jako Priced) – do TypedDict stosujemy prosty adapter
    items: list[CartItem[Priced]] = [
        CartItem(ProductObj(prod1["name"], prod1["price"]), 1),
        CartItem(ProductObj(prod2["name"], prod2["price"]), 1),
        CartItem(ProductObj(prod3["name"], prod3["price"]), 2),
        CartItem(obj, 3),
    ]

    s = subtotal(items)
    print("Subtotal:", format_money(s))

    # Rabaty
    rule10 = flat_pct(0.10)        # -10%
    rule_thr = threshold(300.0, 20.0)  # jeśli >=300 odejmij 20

    after10 = apply_discount(s, rule10)
    after_thr = apply_discount(s, rule_thr)
    after_both = apply_discount(after10, rule_thr)

    print("After -10%:", format_money(after10))
    print("After threshold drop:", format_money(after_thr))
    print("After both:", format_money(after_both))

    # Overloads
    print("Price via overload (TD):", format_money(get_price(prod1)))
    print("Price via overload (Obj):", format_money(get_price(obj)))

    # Lookup
    catalog = {prod1["id"]: prod1, prod2["id"]: prod2, prod3["id"]: prod3}
    print("Lookup existing:", safe_lookup(catalog, ProductID(1)))
    print("Lookup missing:", safe_lookup(catalog, ProductID(999)))

    # Formatowanie Union
    print("Money from float:", format_money(123.456))
    print("Money from int:", format_money(42))
    print("Money from numeric str:", format_money("19,99"))
    print("Money from non-numeric str:", format_money("N/A"))
