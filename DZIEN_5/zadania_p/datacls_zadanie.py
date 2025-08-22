"""
SHAPES BUGGY 
popraw błędy - podziel kod na 4 moduły(pliki pythona) i uruchom

"""

# --- IMPORTY ---
import jsons
from abc import abstractmethod
from dataclasses import dataclass
from typing import List


# --- DATA CLASS ---
@dataclass
class Point:
    x: float
    y: float = "0"   # zły typ domyślnej wartości

    def __post_init__(self):
        # walidacje/konwersje mile widziane
        pass


# --- ABSTRAKCYJNA ---
class Shape:  # brak dziedziczenia z ABC
    name: str

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...

    @abstractmethod
    def to_dict(self) -> dict:
        ...


# --- ZWYKŁA ---
class Circle(Shape):
    def __init__(self, center: Point, radius: float):
        self.name = "circle"
        self.center = center
        self.radius = radius

    def area(self) -> int:     # niespójny typ zwrotny
        return 3.14159 * self.radius  # brak ^2

    def perimeter(self) -> str:  # niespójny typ zwrotny
        return 2 * 3.14159 * self.radius

    def to_dict(self):
        # serializacja do JSON – użyj poprawnych typów
        return {
            "type": self.name,
            "cx": self.center.x,
            "cy": self.center.y,
            "r": str(self.radius)  # string zamiast liczby
        }


# --- I/O ---
def save_to_json(shapes: List[Shape], path: str):
    payload = [s.to_dict() for s in shapes]
    with open(path, "w", encoding="utf-8") as f:
        f.write(jsons.dumps(payload, ensure_ascii=False, indent=2))


# --- MAIN ---
def main():
    print("== SHAPES BUGGY ==")

    # tworzenie obiektów (celowo z typami tekstowymi)
    p = Point("0", "0")
    c = Circle(p, "10")

    # obliczenia i podgląd
    print("center:", p)
    print("area:", c.area())
    print("perimeter:", c.perimeter())

    # zapis
    save_to_json([c], "shapes.json")
    print("Zapisano: shapes.json")


if __name__ == "__main__":
    main()
