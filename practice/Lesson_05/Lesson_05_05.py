#建立預測模型，以房屋資料為例
import pandas
df = pandas.read_csv(r'C:\Projects\training\meterials\tibamepy\data\house-prices.csv')
#print(df.head())
print(df.info())
house = pandas.concat([df, pandas.get_dummies(df['Brick']), pandas.get_dummies(df['Neighborhood'])], axis=1)
del house['No']
del house['West']
del house['Brick']
del house['Neighborhood']
del house['Home']
#print(house.head())

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
X = house[['SqFt', 'Bedrooms', 'Bathrooms','Offers', 'Yes', 'East','North']]
Y = house['Price'].values
regr.fit(X,Y)
print(regr.predict(X))