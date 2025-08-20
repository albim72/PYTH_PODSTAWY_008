# import dane
# import dane as dn
import copy
import math
from dane import liczby, leader, MC as m, kolor
# from dane import *
from mfunkcje.kwadraty import kwadrat,parzyste,slownik

print(liczby)
print("_"*50)
print(leader)
print("_"*50)
print(f"stała MC = {m}")
MC = "listopad"

print(f"stała MC = {MC}")
print(f"stała MC = {m}")

print("_"*50)
print(f"sin(11) = {math.sin(11)}")

print("_"*50)
print(f"kolor z danych: {kolor}")

print("_"*50)
lb = copy.deepcopy(liczby) #kopia głęboka - towrzy nowy obekt typu zadanego - lista z uwzględnieniem zgniezdzeń
print(f"liczby = {lb}")
print(lb is liczby)
print(f"kwadrat(lb) = {kwadrat(lb)}")
print(f"parzyste(lb) = {parzyste(lb)}")
print(f"slownik(leader) = {slownik(leader)}")



