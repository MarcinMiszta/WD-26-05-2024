import pandas as pd

#
# df = pd.read_excel('imiona.xlsx')
# print(df)
# # 1
# print(df[(df.Liczba > 1000)])
# # 2
# print(df[(df.Imie == 'MARCIN')])
# # 3
# print(df[(df.Rok < 2005) & (df.Rok > 2000)].agg({'Liczba': ['sum']}))
# # 4
# print('M', df[(df.Plec == "M")].agg({'Liczba': ['sum']}))
# print('K', df[(df.Plec == "K")].agg({'Liczba': ['sum']}))
# # 5
#
# print("\n")
# # 6
# print(df[(df.Liczba == max(df[(df.Plec == "K")].Liczba))])
# print(df[(df.Liczba == max(df[(df.Plec == "M")].Liczba))])

# zad3

# 1
z = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=',')
z = pd.DataFrame(z)
print(z)
nazwiska = set(z.Sprzedawca)
print(nazwiska)

# 2
print(z.Utarg.astype('float').nlargest(n=5))

# 3

print(z.groupby("Sprzedawca")["idZamowienia"].count())

# 4
print(z.dtypes)
z['Utarg'] = pd.to_numeric(z['Utarg'])
print(z.groupby("Kraj")["Utarg"].sum())

# 5

print(z[(z["Data zamowienia"].astype('datetime64[ns]').dt.year == 2005) & (z['Kraj'] == "Polska")].agg({'Utarg': 'sum'}))
# 6
print(z[(z["Data zamowienia"].astype('datetime64[ns]').dt.year == 2004)]["Utarg"].mean())
#7

dp = z[(z["Data zamowienia"].astype('datetime64[ns]').dt.year==2005)]
dc = z[(z["Data zamowienia"].astype('datetime64[ns]').dt.year==2004)]
dc.to_csv('zamowienia2004.csv', index=False)
dp.to_csv('zamowienia2005.csv', index=False)
