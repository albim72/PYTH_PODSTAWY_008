def przywitaj():
    print("Cześc!")

przywitaj()

def dekorator(funkcja):
    def wrapper():
        print("Początek!")
        funkcja()
        print("Do zobaczenia!")
    return wrapper


#ręczne wywołanie
pr = dekorator(przywitaj)
print("_"*50)
pr()

#deklaratywne użycie
print("_"*50)
@dekorator
def otwarcie():
    print("Otwarcie konkursu!")

otwarcie()
