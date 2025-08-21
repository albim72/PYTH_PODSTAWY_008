from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
    year: int

b1 = Book("Wiedźmin","Andrzej Sapkowski",250,48,1986)
print(b1)
b2 = Book("Hobbit","JRR Tolkien",210,39.95,1937)
print(b2)
