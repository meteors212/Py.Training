# get url content by request.get
import requests
#url="https://tw.appledaily.com/"
url='https://m.thsrc.com.tw/tw/TimeTable/SearchResult'
res = requests.get(url)
#print(res.text)

# get content by post
formeddata = {
    'startStation':'977abb69-413a-4ccf-a109-0272c24fd490',
    'endStation':'3301e395-46b8-47aa-aa37-139e15708779',
    'theDay':'2018/02/04',
    'timeSelect':'11:00',
    'waySelect':'DepartureInMandarin'
}
res = requests.post(url,data=formeddata)
#print(res.text)

# read html innertext content to beautifulsoup using different parser
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'lxml')
#print(soup.text)

soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.text)