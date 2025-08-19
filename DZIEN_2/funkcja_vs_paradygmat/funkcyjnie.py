from functools import reduce

liczby = list(range(1, 11))
print(liczby)

wynik = reduce(
    lambda acc,x: acc + x, #sumowanie kolejnch elementów pobranych z funkcji map
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, liczby)), #funkcja map pobiera elementy z funkcji filter
    # i podnosi do kwadratu, funkcja filter wybiera tylko liczby parzyste z listy
    0 # wynik dla listy pustej
)

print(f"wynik: {wynik}")
