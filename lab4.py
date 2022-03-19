#zad1
# lista = []
# for x in range(0, 31):
#     x*=2
#     lista.append(x)
# plik = open('lista.txt', 'a+')
# plik.writelines(str(lista))
# plik.close()

#zad2
# plik = open('lista.txt', 'r')
# print(plik.readlines())
# plik.close()

#zad3
# with open('lista.txt', 'a+') as plik:
#     for x in range(0, 5):
#         plik.writelines('kilka linijek tekstu \n')
# plik = open('lista.txt', 'r')
# print(plik.readlines())
# plik.close()

#zad4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka, cena):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka = jednostka
#         self.cena = cena
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu + self.ilosc + self.jednostka + self.cena)
#     def ile_produktu(self):
#         print(self.ilosc + self.jednostka)
#     def ile_kosztuje(self):
#         print(self.cena * self.ilosc)

#zad5
# class Ciag:
#     def __init__(self, a1, n, r):
#         self.a1 = a1
#         self.n = n
#         self.r = r
#         self.ciag = (a1 + r * x for x in range(0, n))
#     def wyswietl_dane(self):
#         print(self.ciag)
#     def pobierz_elementy(self, y):
#         if (self.n-1 < y) or (y < 0):
#             print('zle')
#         else:
#             return self.ciag[y]
#     def pobierz_parametry(self, a1, n, r):
#         self.a1 = a1
#         self.n = n
#         self.r = r
#         self.ciag = (a1 + r * x for x in range(0, n))
#     def policz_sume(self):
#         suma = 0
#         for x in range(0, self.n):
#             suma += self.ciag[x]
#         return suma
#     def policz_elementy(self, a1, r):
#         if (self.a1 != '') and (self.r != ''):
#             return self.n

#zad6
class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, ile):
        self.y += ile * self.krok
    def idz_w_dol(self, ile):
        self.y -= ile * self.krok
    def idz_w_lewo(self, ile):
        self.x -= ile * self.krok
    def idz_w_prawo(self, ile):
        self.x += ile * self.krok
    def pokaz_gdzie_jestes(self):
        print(str(self.x) + ', ' + str(self.y))

r = Robaczek(2, 4, 1)
r.pokaz_gdzie_jestes()
r.idz_w_gore(2)
r.idz_w_dol(3)
r.idz_w_lewo(5)
r.idz_w_prawo(1)
r.pokaz_gdzie_jestes()