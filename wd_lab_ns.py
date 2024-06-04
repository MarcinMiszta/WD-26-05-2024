 # import numpy as np
# #
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(a)
# print(b)
#
# c = a - b
# print(c)
#
# print(b**2)
#
# print(a)
# a += b
# print(a)
# a -= b
# print(a)
# d = a*b
# print(d)
# # #
# # # #
# # a = np.arange(12).reshape((3,4))
# # print(a)
# # print(a.sum())
# # print(a.sum(axis=0))
# # print(a.min(axis=1))
# # print(a.cumsum(axis=1))
# # #
# a = np.arange(3)
# b = np.arange(3)
# print(a)
# print(b)
# print(a.dot(b))
# print(np.dot(a,b))
# c = np.array([[1,5], [2, 6], [7, 4]])
# d = np.array([[2,5,4], [4, 3, 1]])
# print(c)
# print(d)
# print(np.dot(c,d))
# print(np.dot(d,c))
# # #
# b = np.arange(3)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))
# c = np.array([2., -1., 4.])
# print(np.add(b,c))
# #
# # a = np.arange(6).reshape((3,2))
# # print(a)
# # print(a.shape)
# # print(type(a.shape))
# # for b in a:
# #     print(b)
# # print('')
# # for i in range(0, a.shape[0]):
# #     for j in range(0, a.shape[1]):
# #         print(a[i][j], end=' ')
# #     print(" ")
# # for b in a.flat:
# #     print(b)
#     # print("")
# #
# # a = np.arange(6).reshape((3,2))
# # print(a)
# # for b in a.flat:
# #     print(b)
# #     # print("")
# #
# a = np.arange(6)
# print(a)
# print(a.shape)
# print("")
# b = a.reshape((2,3))
# print(b)
# print(b.shape)
# print("")
# c = b.reshape((3,2))
# print(c)
# print(c.shape)
# print("")
# d = c.ravel()
# print(d)
# print(d.shape)
# print("")
# e = b.T
# print(e)
# print(e.shape)

# import pandas as pd
# import numpy as np
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['a','b','c','d'])
# print(s)
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)
# df = pd.read_csv('dane.csv',
#                  header=0, sep=";",decimal='.')
# print(df)
# df.to_csv('plik.csv', index=False)
#
# s = pd.Series([10, 12, 8, 14], index=['a','b','c','d'])
# print(s)
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# # print(df)
# print(s['c'])
# print(s.c)
# print(df[0:1])
# print("")
# print(df["Populacja"])
# print(df.iloc[0, 0])
# print(df.loc[0, "Kraj"])
# print(df.at[0, "Kraj"])
# print('kraj: ' + df.Kraj)
# print(df.sample())
#
# print(df.sample(2))
# print(df.sample(frac=0.5))
# print(df.sample(n=10, replace=True))
# print(df.head())
# print(df.head(2))
# print(df.tail(1))
# print(df.describe())
# print(df.T)
#
# s = pd.Series([10, 12, 8, 14], index=['a','b','c','d'])
# print(s)
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
#
# print(s[(s>9)])
# print(s.where(s > 10))
# print(s.where(s>10, 'za duże'))
# seria = s.copy()
# seria.where(seria > 10, 'za duże', inplace=True)
# print("########")
# print(seria)
#
# print(s[~(s > 10)])
#
# print(s[(s < 13) & (s > 8)])
#
# print(df[(df.Populacja > 1000000) & (df.index.isin([0,2]))])
#
# print('#########')
# szukaj = ['Belgia', 'Brasilia']
# print(df.isin(szukaj))
# #
# s['e'] = 15
# print(s.e)
# s['f'] = 16
# print(s)
#
# df.loc[3] = 'dodane'
# print(df)
# df.loc[4] = ['Polska', 'Warszawa', 38675467]
# print(df)
# # #
# new_df = df.drop([3])
# print(new_df)
#
# df.drop([3], inplace=True)
# print(df)
# # #
# # df.drop('Kraj', axis=1, inplace=True)
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
# #
# print(df)

# print(df.sort_values(by='Kraj'))
# grouped = df.groupby(['Kontynent'])
# print(grouped.get_group('Europa'))
# print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
# # print('')
# print(df.groupby(['Kontynent']).agg('Populacja').sum())

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()
#
# print(df)
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)
# # grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0,
# #            legend=True,
# #            title='Populacja z podzałem na kontynenty')
# wykres = grupa.plot.bar()
# wykres.set_ylabel("Mld")
# wykres.set_xlabel('Kontynent')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja z podzałem na kontynenty')
# plt.xticks(rotation=0)
# plt.savefig('wykres.png')

# plt.show()
# #
# df = pd.read_csv('dane.csv', header=0, sep=";",
#                  decimal=".")
# print(df)
# grupa = (df.groupby(['Imię i nazwisko']).
#          agg({'Wartość zamówienia':["sum"]}))
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(6,6), colors=['red', 'green'])
# # wykres = grupa.plot.pie(subplots=True,autopct='%.2f %%',
# #                         fontsize=20, figsize=(6,6))
# plt.legend(loc="lower right")
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()
# #
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# df = pd.DataFrame(ts, columns=['wartości'])
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# plt.plot([1, 2, 3, 4])
# plt.ylabel('jakieś liczby')
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis((0, 6, 0, 20))
# plt.show()
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# # plt.axis((0, 6, 0, 20))
# plt.xlim(0,6)
# plt.ylim(0,20)
# plt.show()

# x = np.linspace(0, 2, 100)
# plt.plot(x, x, 'r--',x, x**2, 'g:')
# # plt.plot(x, x**2, label="kwadratowa")
# # plt.plot(x, x**3, label="sześcienna")
# plt.xlabel('etykieta x')
# plt.ylabel("etykieta y")
# plt.title("Prosty wykres")
# plt.legend(labels=['liniowa', 'kwadratowa'])
# plt.savefig('wykres matplot.png')
# plt.show()
# im1 = Image.open('wykres matplot.png')
# im1 = im1.convert('RGB')
# im1.save('nowy.jpg')

# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label="sin(x)")
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x)')
# plt.legend()
# plt.show()
#
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
# plt.scatter('a', 'b', c='c', cmap='magma', s='d', data=data)
# plt.xlabel('wartość a')
# plt.ylabel('wartość b')
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, '-')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5, left=0.1)
# plt.show()

# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1, '-')
# axs[0, 0].set_title('wykres sin(x)')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_title('wykres cos(x)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_title('wykres cos(x)')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# #
# plt.show()



# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = np.array(list(grupa.groups.keys()))
# wartosci = list(grupa.agg('Populacja').sum())
# fig, ax = plt.subplots()
# ax.bar(x=etykiety, height=wartosci, color=['yellow', 'green', 'red'])
# ax.set_xlabel('Kontynenty')
# ax.set_ylabel('Populacja w mld')
# ax.ticklabel_format(axis='y', style='plain')
# fig.subplots_adjust(left=0.2)
# plt.show()


df = pd.read_csv('dane.csv', header=0, sep=";",
                 decimal=".")
print(df)
seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
print(seria)
wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
                                  autopct=lambda pct: "{:.1f}%".
                                  format(pct),
                                  textprops=dict(color="black"),
                                  colors=['red', 'green'])
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()
