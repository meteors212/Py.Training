#用AIC挑出變數最適合的模型，數值越小越好
import itertools
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

predictorcols = ['sqft', 'bedrooms', 'bathrooms', 'offers', 'yes', 'East', 'North', "East", "West", "South"]
df = pandas.read_csv(r'C:\Projects\training\meterials\tibamepy\data\house-prices.csv')
AICs = {}
X = house[['SqFt', 'Bedrooms', 'Bathrooms','Offers', 'Yes', 'East','North']]
Y = house['Price'].values
for k in range(1,len(predictorcols)+1):
    for variables in itertools.combinations(predictorcols, k):
        predictors = X[list(variables)]
        predictors2 = sm.add_constant(predictors)
        est = sm.OLS(Y, predictors2)
        res = est.fit()
        AICs[variables] = res.aic