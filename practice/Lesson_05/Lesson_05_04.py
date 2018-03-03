#回歸分析
import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv(r'C:\Projects\training\meterials\tibamepy\data\salary.csv', index_col=0)

from matplotlib import pyplot as plt
X = df[['year']]
Y = df['salary'].values
plt.scatter(X, Y, color='black')
plt.xlabel('year')
plt.ylabel('salary')
#plt.show()

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X,Y)

print('Coefficients:', regr.coef_)
print('Intercept:', regr.intercept_)
plt.scatter(X, Y, color='black')
plt.plot(X, regr.predict(X), color='blue', linewidth=3)
#plt.show()


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg = PolynomialFeatures(degree=2)
X_ = poly_reg.fit_transform(X)
regr = LinearRegression()
regr.fit(X_, Y)

X2 = X.sort_values(['year'])
X2_ = poly_reg.fit_transform(X2)
plt.scatter(X, Y, color='black')
plt.plot(X2, regr.predict(X2_), linewidth = 3,
color="blue")
plt.show()