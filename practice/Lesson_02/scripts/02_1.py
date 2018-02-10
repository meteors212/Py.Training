import requests
import pandas
from bs4 import BeautifulSoup
import os

def GetHouseTransactionTable():
    url = ''
    req = requests.get(url)
    html = BeautifulSoup(req.text)
    houseDic = {}

    houselist = html.select('div')
    for house in houselist:
        houseDic[house.text] = house.attrs[''].text

    outputPath = os.path.dirname(os.path.dirname(os.path.realpath('_file_'))) + 'output'
    os.path.d
    df = pandas.DataFrame(houseDic)
    df.to_excel()