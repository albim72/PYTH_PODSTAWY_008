from functools import reduce

liczby = list(range(1, 11))
print(liczby)

wynik = reduce(
    lambda acc,x: acc + x,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, liczby)),
    0
)

print(f"wynik: {wynik}")
