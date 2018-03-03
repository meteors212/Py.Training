import pandas
import matplotlib.pyplot as plt
tw2330 = pandas.read_csv(r'C:\Projects\training\meterials\tibamepy\data\tw2330.csv', parse_dates={'Dates': [0]})
#print(tw2330.info())  # to concise dataframe info
#print(tw2330.describe())
#print(tw2330.dtypes)

tw2330.dropna(inplace=True)
#tw2330 = tw2330[tw2330['Close'] != 'null']
tw2330['Close'] = tw2330['Close'].astype(float)
tw2330['Open'] = tw2330['Open'].astype(float)
tw2330['High'] = tw2330['High'].astype(float)
tw2330['Low'] = tw2330['Low'].astype(float)

tw2330['Close'] .max()
tw2330['Close'] .min()
tw2330['Close'] .mean()
tw2330['Close'] .count()
#print(tw2330.head())
#print(tw2330.tail())

#print(tw2330["Close"].mean())
'''
a = [0,42,50,60,55,72,58,80,82,87,98]
sa = pandas.Series(a)
plt.plot(a)
plt.legend
plt.show()
'''

print(tw2330["Close"].var())

