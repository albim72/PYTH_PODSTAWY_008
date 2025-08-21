from dataclasses import dataclass

#definicja zwykłej klasy pythona
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

#definicja klasy danych
@dataclass
class ProductDataclass:
    name: str
    price: float


#utworzenie obiektów
#obiekt klasy Product
p1 = Product("chleb", 4.5)
print(p1)

#obiekt klasy ProductDataclass
p2 = ProductDataclass("mleko", 5.11)
print(p2)
