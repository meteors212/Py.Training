#homework
import pandas
house = pandas.read_csv(r'C:\Projects\training\meterials\tibamepy\data\rent_591_sample.csv', index_col=0)
#print(house.head(3))

# 資料清理: 把奇怪的逗點去掉
house['price'] = house['price'].map(lambda e: int(str(e).replace(',', '')))
#print(house['price'].head())

house[['bedroom', 'livingroom', 'bathroom']] = house['layout'].str.extract('(\d+)房(\d+)廳(\d+)衛')
#print(house.head())

house = house[['price', 'area', 'bathroom', 'livingroom', 'bedroom', 'floor', 'allfloor']]
#print(house.head())

house['bathroom'] = house['bathroom'].astype(float)
house['livingroom'] = house['livingroom'].astype(float)
house['bedroom'] = house['bedroom'].astype(float)

house.dropna(inplace=True)

X = house[['area', 'bathroom', 'livingroom', 'bedroom', 'floor', 'allfloor']]
y = house['price']

import statsmodels.api as sm
X2 = sm.add_constant(X)