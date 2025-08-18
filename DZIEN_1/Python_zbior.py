drzewa = {"jodła","dąb","buk","jabłoń","olcha","dąb"}
print(drzewa)
print(drzewa)
print(drzewa)
print(type(drzewa))

drzewa.add("wierzba")
print(drzewa)

drzewa.discard("olcha")
print(drzewa)

drzewa.discard("baobab")
print(drzewa)

dr = list(drzewa)
dr.sort()
print(dr)

# drzewa.sort()
print(sorted(drzewa))

print(type(sorted(drzewa)))
print(type(drzewa))

#uczestnicy warsztatów ceramiki
warsztat1 = ["Ala","Bartek","Celina","Ala","Darek","Urszula","Tomasz"]
warsztat2 = ["Celina","Ewa","Filip","Bartek","Filip","Tomasz","Euzebiusz"]

#zmiana list na zbiory
uczestnicy1 = set(warsztat1)
uczestnicy2 = set(warsztat2)

print(uczestnicy1)
print(uczestnicy2)
#kto brał udział w obu wydarzeniach na raz
print(uczestnicy1.intersection(uczestnicy2))
wspolne = uczestnicy1 & uczestnicy2
print(wspolne)

#kto był tylko ma 1 warsztaccie?
pierwszy = uczestnicy1 - uczestnicy2
print(pierwszy)

#ile fiycznie osob brał oudział w obu warsztatach
wszyscy = uczestnicy1 | uczestnicy2
print(wszyscy)

#zbiór zamorożony
zmarozony = frozenset(uczestnicy1)
print(zmarozony)

# zmarozony.add("Grzegorz")
