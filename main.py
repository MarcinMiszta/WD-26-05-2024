from numpy import *
import pandas as pd

# a = array([20, 30, 40, 50])
# b = arange(4)
#
# print(a)
# print(b)
#
# c = a - b
# print(c)
#
# print(b ** 2)
#
# print(a)
# a += b
# print(a)
# a -= b
# print(a)
# d = a * b
# print(d)
#
# b = arange(3)
# print(b)
# print(exp(b))
# print(sqrt(b))
# c = array([2, -1, 4])
# print(add(b, c))

# a = arange(12).reshape(3, 4)
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.min(axis=1))
# print(a.cumsum(axis=1))

# a = arange(3)
# b = arange(3)
# print(a)
# print(b)
# print(a.dot(b))
# print(dot(a, b))
#
# c = array([[1, 5], [2, 6], [7, 4]])
# d = array([[2, 5, 4], [4, 3, 1]])
# print(c)
# print(d)
# print(dot(c, d))
# print(dot(d, c))

# a=arange(6).reshape((3,2))
# print(a)
# print(a.shape)
# print(type(a.shape))
# for b in a:
#     print(b)
# print("")
# for i in range(0, a.shape[0]):
#     for j in range(0, a.shape[1]):
#         print(a[i][j], end="")
#     print(" ")
# for b in a.flat:
#     print(b)

# a = arange(6)
# print(a)
# print(a.shape)
# print("")
# b = a.reshape((2, 3))
# print(b)
# print(b.shape)
# print("")
# c = b.reshape((3, 2))
# print(c)
# print(c.shape)
# print("")
# d = c.ravel()
# print(d)
# print(d.shape)
# print("")
# d = c.ravel()
# print(d)
# print(d.shape)
# print("")

s = pd.Series([1, 3, 5, nan, 6, 8])
print(s)
s = pd.Series([1, 20, 3, 40], index=['a', 'b', 'c', 'd'])
print(s)
data = {'kraj': ['belgia', 'polska', 'uk'], 'stolica': ['bruksela', 'warszawa', 'londyn'],
        'populacja': [111908462, 400000000, 511908462]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# df.to_csv('plik.csv', index=False)

# print(s['c'])
# print(s.c)
# print(df[0:1])
# print('')
# print(df['populacja'])
# print(df.iloc[0, 0])
# print(df.loc[0, 'kraj'])
# print(df.at[0, 'kraj'])
# print('kraj: ' + df.kraj)
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

# print(s[(s > 9)])
# print(s.where((s >= 10)))
# print(s.where(s > 10, 'za duze'))
# seria = s.copy()
# seria.where((s >= 10), 'za duze', inplace=True)
# print('#########')
# print(seria)

print(s[~(s > 10)])
print(s[(s < 13) & (s > 8)])

print(df[(df.populacja > 1000000) & (df.index.isin([0, 2]))])

print('###########')
szukaj = ['belgia', 'polska']
print(df.isin(szukaj))

s['e'] = 15
print(s.e)
s['f'] = 16
print(s)

df.loc[3] = 'dodane'
print(df)
df.loc[4] = ['Polska', 'Warszawa', 38000000]
print(df)

new_df = df.drop([1])
print(new_df)

df.drop([3],inplace=True)
print(df)

df.drop('kraj',axis=1,inplace=True)
df['kontynent']=['europa','azja','ameryka poludniowa','europa']
print(df)

