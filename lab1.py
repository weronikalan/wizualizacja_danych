# #zad1
# a, b = 1, 2
# print(a, b)
#
# c, d = 1.2, 3.4
# print(c, d)
#
# e, f = 1+2j, 3+4j
# print(e, f)
#
# #zad2
# liczba1 = int(input("Pierwsza liczba:"))
# liczba2 = int(input("Druga liczba:"))
# znak = input("Znak działania(+,-,*,/,**)")
#
# słownik = {"+": liczba1+liczba2, "-": liczba1-liczba2, "*": liczba1*liczba2, "/": liczba1/liczba2, "**": liczba1**liczba2}
#
# if znak == "+":
#     print(słownik["+"])
# elif znak == "-":
#     print(słownik["-"])
# elif znak == "*":
#     print(słownik["*"])
# elif znak == "/":
#     print(słownik["/"])
# elif znak == "**":
#     print(słownik["**"])
# else:
#     print("Błędny znak")

#zad3
# a=1
# a+=1
# print(a)
#
# b=2
# b-=1
# print(b)
#
# c=2
# c*=2
# print(c)
#
# d=4
# d/=2
# print(d)
#
# e=3
# e**=2
# print(e)
#
# f=20
# f%=100
# print(f)


#zad4
# import math
# print(math.e**10)
# print((math.log(5)+(math.sign(8)**2))**(1/6))
# print(math.floor(3.55))
# print(math.ceil(4.80))

# #zad5
# a = 'WERONIKA'
# b = 'ŁANIEWSKA'
# print("a.capitalize() : " , a.capitalize())
# print("b.capitalize() : " , b.capitalize())

# #zad6
# tekst = 'Ala la la ma la la la kota'
# print("tekst.count('la') : " , tekst.count('la'))

#zad7
# imie = 'Weronika'
# print(imie[1], imie[7])

#zad8
# tekst = 'Ala la la ma la la la kota'
# print(tekst.split(' '))

#zad9
# a = '1234'
# b = 1
# c = 10
#
# print('%(a)s'%{'a':a})
# print('%(b)f'%{'b':b})
# print('%(c)x'%{'c':c})