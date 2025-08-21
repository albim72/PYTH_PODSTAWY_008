from __future__ import annotations
from dataclasses import dataclass, field, asdict, replace
from enum import Enum, auto
from datetime import datetime, timezone
from typing import List, Iterable, Dict
from uuid import UUID, uuid4
import json

# === MODELE DANYCH (dataclasses) ============================================

@dataclass(frozen=True, slots=True)
class Address:
    street: str
    city: str
    country: str = "PL"

    def pretty(self) -> str:
        return f"{self.street}, {self.city}, {self.country}"


@dataclass(frozen=True, slots=True)
class Customer:
    id: UUID
    name: str
    email: str
    address: Address

    def __post_init__(self):
        if "@" not in self.email:
            raise ValueError("Invalid email")


@dataclass(order=True, frozen=True, slots=True)
class Product:
    # order=True → można sortować produkty po polach w kolejności deklaracji
    sku: str
    name: str
    price: float        # netto
    vat: float = 0.23   # 23% VAT domyślnie

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("price must be >= 0")
        if not (0.0 <= self.vat < 1.0):
            raise ValueError("vat must be in [0,1)")


@dataclass(slots=True)
class CartItem:
    product: Product
    qty: int
    discount_pct: float = 0.0  # 0..1

    def __post_init__(self):
        if self.qty < 1:
            raise ValueError("qty must be >= 1")
        if not (0.0 <= self.discount_pct < 1.0):
            raise ValueError("discount_pct must be in [0,1)")

    @property
    def net_unit(self) -> float:
        return self.product.price * (1.0 - self.discount_pct)

    @property
    def gross_unit(self) -> float:
        return self.net_unit * (1.0 + self.product.vat)

    @property
    def line_total_net(self) -> float:
        return self.net_unit * self.qty

    @property
    def line_total_gross(self) -> float:
        return self.gross_unit * self.qty

    def with_qty(self, qty: int) -> "CartItem":
        # immutacyjny „builder”: zwróć kopię z inną ilością
        return replace(self, qty=qty)


class OrderStatus(Enum):
    DRAFT = auto()
    CONFIRMED = auto()
    CANCELLED = auto()


@dataclass(slots=True)
class Order:
    customer: Customer
    items: List[CartItem] = field(default_factory=list)
    status: OrderStatus = field(default=OrderStatus.DRAFT)
    id: UUID = field(default_factory=uuid4, init=False)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc), init=False)

    _total_net: float = field(default=0.0, init=False, repr=False)
    _total_gross: float = field(default=0.0, init=False, repr=False)

    # --- logika domenowa (metody) ---
    def add_item(self, item: CartItem) -> None:
        self._ensure_draft()
        self.items.append(item)
        self._recalc()

    def remove_by_sku(self, sku: str) -> None:
        self._ensure_draft()
        before = len(self.items)
        self.items = [i for i in self.items if i.product.sku != sku]
        if len(self.items) == before:
            raise KeyError(f"Item with SKU {sku} not found")
        self._recalc()

    def change_qty(self, sku: str, qty: int) -> None:
        self._ensure_draft()
        found = False
        for idx, it in enumerate(self.items):
            if it.product.sku == sku:
                self.items[idx] = it.with_qty(qty)
                found = True
                break
        if not found:
            raise KeyError(f"Item with SKU {sku} not found")
        self._recalc()

    def confirm(self) -> None:
        self._ensure_draft()
        if not self.items:
            raise ValueError("Cannot confirm empty order")
        self.status = OrderStatus.CONFIRMED

    def cancel(self) -> None:
        if self.status is OrderStatus.CANCELLED:
            return
        if self.status is OrderStatus.CONFIRMED:
            # biznesowo: np. nie wolno anulować po wysyłce – tu tylko przykład
            pass
        self.status = OrderStatus.CANCELLED

    @property
    def total_net(self) -> float:
        return round(self._total_net, 2)

    @property
    def total_gross(self) -> float:
        return round(self._total_gross, 2)

    def _recalc(self) -> None:
        self._total_net = sum(i.line_total_net for i in self.items)
        self._total_gross = sum(i.line_total_gross for i in self.items)

    def _ensure_draft(self) -> None:
        if self.status is not OrderStatus.DRAFT:
            raise RuntimeError("Order is not editable outside DRAFT")

    # --- (de)serializacja lekkiego DTO ---
    def to_dict(self) -> Dict:
        # asdict działa dobrze dla dataclass, ale mamy też UUID/datetime
        d = asdict(self)
        d["id"] = str(self.id)
        d["created_at"] = self.created_at.isoformat()
        d["status"] = self.status.name
        # dopiszemy dodatkowo total* (wyliczane)
        d["total_net"] = self.total_net
        d["total_gross"] = self.total_gross
        return d


# === WARSTWY APLIKACYJNE (klasy zwykłe) ====================================

class InMemoryOrderRepository:
    """Zwykła klasa: repozytorium (brak dataclass, bo trzyma stan i ma logikę)."""
    def __init__(self):
        self._db: Dict[UUID, Order] = {}

    def save(self, order: Order) -> None:
        self._db[order.id] = order

    def get(self, order_id: UUID) -> Order:
        try:
            return self._db[order_id]
        except KeyError:
            raise KeyError("Order not found")

    def list_all(self) -> Iterable[Order]:
        return list(self._db.values())


class OrderService:
    """Zwykła klasa: reguły biznesowe/operacyjne nad modelami dataclass."""
    def __init__(self, repo: InMemoryOrderRepository):
        self.repo = repo

    def create_order(self, customer: Customer) -> Order:
        order = Order(customer=customer)
        self.repo.save(order)
        return order

    def add_line(self, order_id: UUID, item: CartItem) -> Order:
        order = self.repo.get(order_id)
        order.add_item(item)
        self.repo.save(order)
        return order

    def apply_cart_discount(self, order_id: UUID, pct: float) -> Order:
        """Przykładowa operacja: globalny rabat jako modyfikacja pozycji."""
        if not (0.0 <= pct < 1.0):
            raise ValueError("pct must be in [0,1)")
        order = self.repo.get(order_id)
        order._ensure_draft()
        order.items = [
            replace(it, discount_pct=min(0.99, it.discount_pct + pct)) for it in order.items
        ]
        order._recalc()
        self.repo.save(order)
        return order

    def confirm(self, order_id: UUID) -> Order:
        order = self.repo.get(order_id)
        order.confirm()
        self.repo.save(order)
        return order


# === PRZYKŁADOWE UŻYCIE =====================================================

if __name__ == "__main__":
    # Klient i adres (dataclasses zamrożone)
    addr = Address("Królewska 10", "Warszawa")
    cust = Customer(id=uuid4(), name="Marcin Albiniak", email="marcin@example.com", address=addr)

    # Produkty (zamrożone, porównywalne)
    p_book = Product(sku="B-001", name="AI in Practice", price=120.0, vat=0.05)
    p_head = Product(sku="E-777", name="Headphones Pro", price=299.99)  # 23% VAT domyślnie

    # Repo + serwis (klasy zwykłe)
    repo = InMemoryOrderRepository()
    svc = OrderService(repo)

    # Tworzymy zamówienie
    order = svc.create_order(cust)
    print("New order:", order.id)

    # Dodajemy pozycje (dataclass CartItem)
    svc.add_line(order.id, CartItem(product=p_book, qty=2, discount_pct=0.10))
    svc.add_line(order.id, CartItem(product=p_head, qty=1))

    # Prosty rabat koszykowy (logika w klasie zwykłej)
    svc.apply_cart_discount(order.id, 0.05)  # +5% do istniejących rabatów pozycji

    # Podsumowanie
    order = repo.get(order.id)
    print("Items:", len(order.items))
    print("Total NET :", order.total_net)
    print("Total GROSS:", order.total_gross)

    # Zatwierdzenie
    svc.confirm(order.id)
    print("Status:", order.status)

    # (De)serializacja DTO do JSON (np. zapis do logów / API)
    payload = order.to_dict()
    print(json.dumps(payload, ensure_ascii=False, indent=2))
