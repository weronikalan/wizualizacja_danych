#zad1
# lista = ['siatkówka', 'piłka nożna', 'koszykówka']
# lista.reverse()
# lista.append('tenis')
# lista.append('bieganie')
# print(lista)

#zad2
# słownik = {'itp':'i tym podobne', 'itd':'i tak dalej', 'k.p.':'kodeks pracy'}
# print(słownik)

#zad3
# słownik = {'gra1':'Minecraft', 'gra2':'Counter-Strike', 'gra3':'Far Cry'}
# print(słownik.count())

#zad4
# zdanie = input('Zdanie:' )
# print(zdanie)
# litera = 0
# for char in zdanie:
#     if char == 'a':
#         litera+=1
# print(litera)

#zad5
# import sys as system
# a = (system.stdin.readline())
# b = (system.stdin.readline())
# c = (system.stdin.readline())
# wynik = a**b+c
# system.stdout.write(str(wynik))

#zad6
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if a > b:
#     if a > c:
#         maks = a
#         print('największa: ',(maks))
#     else:
#         maks = c
# elif b > a:
#     if b > c:
#         maks = b
#         print('największa: ',(maks))
#     else:
#         maks = c
#         print('największa: ',(maks))

#zad7
# lista1 = [2, 3.0, 4, 5.0]
# lista2 = []
# print(lista1)
# for i in range(len(lista1)):
#     lista2.append(lista1[i]**2)
# print(lista2)

#zad8
# lista = []
# for i in range(1, 11):
#     print(i)
# ilość = 0
# while ilość < 10:
#     ilość += 1
#     if i % 2 == 0:
#         lista.append(i)
# print(lista)

#zad9
# import math
# liczba = int(input('Podaj liczbę: '))
# try:
#     print(math.sqrt(liczba))
# except ValueError:
#     print('Podałeś ujemną liczbę')