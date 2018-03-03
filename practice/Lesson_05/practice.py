import pandas
tw2330 = pandas.read_csv(r"C:\Projects\training\meterials\tibamepy\data\tw2330.csv", parse_dates={'Dates':[0]})
#print(tw2330.info())
#print(tw2330.describe())
# === 資料清理 ===
tw2330.dropna(inplace=True)
tw2330 = tw2330[tw2330["Close"] != 'null']
tw2330['Close'] = tw2330['Close'].astype(float)
tw2330['Open'] = tw2330['Open'].astype(float)
tw2330['High'] = tw2330['High'].astype(float)
tw2330['Low'] = tw2330['Low'].astype(float)
#=== 求收盤價統計值 ===
print(tw2330['Close'].mean()) #平均數
print(tw2330['Close'].min()) #最小
print(tw2330['Close'].max()) #最大
print(tw2330['Close'].count()) #數量

