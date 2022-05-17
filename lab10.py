import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#zad1
# x = np.arange(1, 20, 1)
# y = []
# for i in x:
#     y.append(1/i)
#
# plt.plot(x, y)
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.legend(labels = ['f(x) = 1/x'])
# plt.show()

#zad2
# x = np.arange(1, 20, 1)
# y = []
# for i in x:
#     y.append(1/i)
#
# plt.plot(x, y, 'g:', x, y, 'g^')
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.legend(labels = ['f(x) = 1/x'])
# plt.show()

#zad3
# x = np.arange(0, 30, 0.01)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.plot(x, y1, 'r', x, y2, 'g')
# plt.ylabel('y')
# plt.xlabel('x')
# plt.legend(labels = ['sin', 'cos'])
# plt.show()

#zad4


#zad5
# df = pd.read_csv('imiona.xlsx', header=0, sep=";", decimal=".")
# print(df)
# grupa = df.groupby('Plec')
# wartosc = list(grupa.agg('Liczba').sum())
#
# plt.bar(x='Plec', height=wartosc, color=['blue', 'red'])
# plt.xlabel('Plec')
# plt.ylabel('Liczba')
# plt.show()

#zad6
df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=".")
print(df)
seria = df.groupby('Sprzedawca')['Utarg'].sum()
df.explode('Sprzedawca')
wedges, texts, autotext = plt.pie(x=seria, labels=seria.index, autopct=lambda pct:
"{:.1f}%".format(pct), textprops=dict(color="black"), colors=['blue', 'red', 'green', 'yellow', 'pink', 'orange', 'grey', 'purple', 'lightblue'])

plt.title('Suma zamówień')
plt.legend(loc='lower right', shadow=True)
plt.ylabel('Procentowy wynik')
plt.show()