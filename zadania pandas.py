import pandas as pd

df = pd.read_excel('imiona.xlsx')
print(df)
# 1
print(df[(df.Liczba > 1000)])
# 2
print(df[(df.Imie == 'MARCIN')])
# 3
print(df[(df.Rok < 2005) & (df.Rok > 2000)].agg({'Liczba': ['sum']}))
# 4
print('M', df[(df.Plec == "M")].agg({'Liczba': ['sum']}))
print('K', df[(df.Plec == "K")].agg({'Liczba': ['sum']}))
# 5
print(df.groupby(['Rok']).)
# 6
print(df[(df.Liczba == max(df[(df.Plec == "K")].Liczba))])
print(df[(df.Liczba == max(df[(df.Plec == "M")].Liczba))])
