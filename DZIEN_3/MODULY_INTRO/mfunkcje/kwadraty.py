def kwadrat(lista):
    return [x**2 for x in lista]

def parzyste(lista):
    return [x%2==0 for x in lista]

def slownik(dct):
    return [f"{x}: {y}" for x,y in dct.items()] #dct.items() - pobieranie pary klucz-wartośc ze słownika
        #przekazywanie pary do pętli element za elementem, nastpnie wstawianie do listy stringów f"{x}: {y}"
