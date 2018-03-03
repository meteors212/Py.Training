#計算台積電與大盤的相關程度
import  pandas
twii = pandas.read_csv('https://raw.githubusercontent.com/ywchiu/tibamepy/master/data/TWII.csv', parse_dates={'Dates': [0]})
tw2330 = pandas.read_csv('https://raw.githubusercontent.com/ywchiu/tibamepy/master/data/tw2330.csv',parse_dates={'Dates':[0]})

m = pandas.merge(twii, tw2330, left_on="Dates", right_on="Dates")

m = m[["Dates", "Close_x", "Close_y"]]
m.columns = ['Dates', 'TWII', 'TW2330']
m2 = m[ (m['TWII'] != 'null') & (m['TW2330'] != 'null') ]
m2['TWII'] = m2['TWII'].astype(float)
m2['TW2330'] = m2['TW2330'].astype(float)

print(m2[['TWII', 'TW2330']].corr())
'''
m2['TWII'] = m2['TWII'].astype(float)
m2['TW2330'] = m2['TW2330'].astype(float)

print(m2[['TWII', 'TW2330']].corr())
'''
