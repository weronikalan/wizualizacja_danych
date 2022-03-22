#zad1
# A = [1 - x for x in range(0, 11)]
# print(A)
# B = [4 ** x for x in range(0, 8)]
# print(B)
# C = [x for x in B if x % 2 == 0]
# print(C)

#zad2
# import random
# lista1 = []
# for i in range(0, 11):
#     lista1.append(random.randint(0, 20))
# print(lista1)
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista2)

#zad3
# słownik = {'woda': 'l', 'bułki': 'szt', 'ziemniaki': 'kg'}
# lista = [a for (a,b) in słownik.items() if b == 'szt']
# print(lista)


#zad4
# def trojkat(a, b, c):
#     if ((a+b>c) and (a+c>b) and (b+c>a)):
#         if ((a*a+b*b==c*c) or (a*a+c*c==b*b) or (c*c+b*b==a*a)):
#             print("To jest trójkąt prostokątny")
#         else:
#             print("To nie jest trójkąt prostokątny")
#     else:
#         print("Nie można zbudować trójkąta")
#
# trojkat(2, 3, 4)
# trojkat(2, 5, 10)
# trojkat(8, 15, 17)

#zad5
# import math
# def trapez(a = 10, b = 7, h = 4):
#     return ((a + b) * h / 2)
# print(trapez())

#zad6
# def ciag(a = 1, b = 4, ile = 10):
#     wynik = a
#     elementy = []
#     for x in range(ile):
#         x = a + x * b
#         elementy.append(x)
#         wynik *= x
#     print(elementy)
#     return wynik
#
# print(ciag())

#zad7
# import math
# def ciag(* a):
#     if len(a) == 0:
#         return 0
#     else:
#         elementy = [x for x in a]
#         iloczyn = 1
#         for x in a:
#             iloczyn *= x
#         return iloczyn
#
# print(ciag(1, 3, 5, 7))

#zad8
# def funkcja(** produkty):
#     ilosc = 0
#     cena = 0
#     for x in produkty:
#         ilosc += 1
#         cena += produkty[x]
#     print('ilosc: ', ilosc)
#     print('cena: ', cena)
#
# funkcja(czekolada = 3.0, woda = 0.99, ser = 4.50)

#zad9
from zad9 import c_aryt
from zad9 import c_geom
c_aryt.aryt()
c_geom.geom()