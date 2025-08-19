class Book:
    __kolor = "czerwony"
    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(Book)
    
    def __init__(self,title,author,price,pages,bookstore_nb):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.bookstore_nb = bookstore_nb
        self.binding = "miękka"
        self.newboook()

    def __repr__(self):
        return (f"tytuł: {self.title} - autor:{self.author}, cena: {self.price},liczba stron: {self.pages}"
                f"nr księgarni: {self.bookstore_nb}, oprawa: {self.binding}")

    def get_binding(self):
        return self.binding

    def set_binding(self,binding):
        self.binding = binding

    def newboook(self):
        print("Nowy obiekt klasy Book został utworzony!")

    def cena_rabat(self,procent):
        self.price = self.price - (self.price*procent/100)
        return self.price

    def obwoluta(self):
        return self.__kolor


b = Book("ABC biegacza ultra","Jurek Scott",102,324,22)
print(b)
print(b.get_binding())
b.set_binding("twarda")
print(b.get_binding())
print(f"cena po rabacie: {b.cena_rabat(12)} zł")
print(f"kolor obwoluty: {b.obwoluta()}")
