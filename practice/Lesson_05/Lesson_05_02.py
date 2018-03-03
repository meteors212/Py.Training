#?pandas.read_csv
import pandas
tw2330 = pandas.read_csv('https://raw.githubusercontent.com/ywchiu/tibamepy/master/data/tw2330.csv',\
                         parse_dates={'Dates':[0]})
tw2330 = tw2330[tw2330['Close'] != 'null']
tw2330['Close'] =tw2330['Close'].astype(float)
print(tw2330.info())