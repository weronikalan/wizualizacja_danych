import numpy as np

#zad1
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = a * b
# print(c)

#zad2
# a = np.arange(9).reshape((3, 3))
# b = np.arange(16).reshape((4, 4))
# print(np.min(a, axis=0))
# print(np.min(a, axis=1))
# print(np.min(b, axis=0))
# print(np.min(b, axis=1))

#zad3
# print(a*b)

#zad4
# a = np.array([1, 2, 3])
# b = np.array([4.2, 5.7, 6.9])
# c = a * b
# print(c)

#zad5
# mac = np.array([[1, 2, 6], [3, 4, 5]])
# a = np.sin(mac)
# print(a)
#
# #zad6
# mac2 = np.array([[6, 7, 5], [8, 9, 3]])
# b = np.cos(mac2)
# print(b)
#
# #zad7
# def funkcja(a, b):
#     c = a + b
#     return c
#
# a = np.sin(mac)
# b = np.cos(mac2)
# print(funkcja(a, b))

#zad8
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# for i in a:
#     print(i)

#zad9
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# for i in a.flat:
#     print(i)

#zad10
# a = np.arange(81).reshape((9, 9))
# print(a)

#zad11
a = np.arange(12)
print(a)
b = a.reshape((3, 4))
print(b)
c = b.reshape((4, 3))
print(c)
d = c.reshape((2, 6))
print(d)

b2 = b.ravel()
print(b2)
c2 = c.ravel()
print(c2)
d2 = d.ravel()
print(d2)