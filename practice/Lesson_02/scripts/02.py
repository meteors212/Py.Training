# get url content by request.get
import requests
import os

def ParseHTMLContent():
    # read html content in file
    dirpath = os.path.dirname(os.path.dirname(os.path.realpath('_file_')))
    testFilePath = os.path.join(dirpath, r'data\test.html')

    with open(testFilePath) as html:
        res = html.read()
        #print(res)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(res, 'lxml')
    alist = soup.find_all('a')
    for a in alist:
        print(a)

##================================================
    #read html content from http request
    '''
    url="https://tw.appledaily.com/"
    url='https://m.thsrc.com.tw/tw/TimeTable/SearchResult'
    res = requests.get(url)
    print(res.text)
        '''


    # get content by post
    '''
        formeddata = {
            'startStation':'977abb69-413a-4ccf-a109-0272c24fd490',
            'endStation':'3301e395-46b8-47aa-aa37-139e15708779',
            'theDay':'2018/02/04',
            'timeSelect':'11:00',
            'waySelect':'DepartureInMandarin'
     }
    res = requests.post(url,data=formeddata)
    print(res.text)
    '''

    # read html innertext content to beautifulsoup using different parser
    '''
    #from bs4 import BeautifulSoup
    #soup = BeautifulSoup(res.text, 'lxml')
    #print(soup.text)

    #soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup.text)
    #alist = soup.select('a')
    #for a in alist:
    #    print(a.text)
    '''


ParseHTMLContent()