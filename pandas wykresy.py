import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#
# df = pd.read_excel('imiona.xlsx')
# print(df)
#
# # zad1
#
# liczba_dzieci = df.groupby(["Rok"]).agg({'Liczba': ['sum']})
# wykres = liczba_dzieci.plot.bar()
# wykres.set_title('Liczba urodzonych dzieci z podziałem na lata')
# wykres.set_xlabel('Rok')
# wykres.set_ylabel('Liczba urodzonych dzieci')
# wykres.legend()
# plt.subplots_adjust(top=0.9, left=0.2)
# plt.show()
# print(liczba_dzieci)
#
# # zad2
#
# liczba_dzieci2 = df.groupby(["Plec"]).agg({'Liczba': ['sum']})
# wykres = liczba_dzieci2.plot.bar()
# wykres.ticklabel_format(style='plain', axis='y', scilimits=(0, 0))
# plt.show()
#
# # zad 3
# liczba_dzieci5 = df[(df.Rok == 2017) | (df.Rok == 2016) | (df.Rok == 2015) | (df.Rok == 2014) | (df.Rok == 2013)].groupby(["Plec"])['Liczba'].sum()
# print(liczba_dzieci5)
# wedges, texts, autotexts = plt.pie(x=liczba_dzieci5, labels=liczba_dzieci5.index,
#                                    autopct=lambda pct: "{:.1f}%".format(pct),
#                                    textprops=dict(color='black'), colors=['green', 'red'])
# plt.legend()
# plt.title("Liczba urodzonych")
# plt.ylabel("Procentowy udział")
# plt.show()

#zad 4
df=pd.read_csv("zamowienia.csv", index_col=0, sep=';', decimal='.')
print(df)
ilosc = df.groupby(["Sprzedawca"])['idZamowienia'].count()
wykres = ilosc.plot.bar()
wykres.set_title("Sprzedawcy i zamowienia")
wykres.set_xlabel("Sprzedawca")
wykres.set_ylabel("Ilość zamowień")
plt.subplots_adjust( bottom=0.25, left=0.15)
plt.savefig("wykresy.png")
plt.show()
print(ilosc)