def Get_Agile_Data():
    from selenium import webdriver
    import time
    chrome_path = r'C:\selenium\chromedriver.exe'
    browser = webdriver.Chrome(chrome_path)

    browser.get('https://agile.us.dell.com/Agile/PLMServlet?module=LoginHandler&opcode=handlePopupBlocker')
    time.sleep(5)

    ## login
    browser.find_element_by_id('j_username').send_keys('yoyo_z_zhang@wistron.com') #set account
    browser.find_element_by_id("j_password").send_keys('Linna2041') #set password
    browser.find_element_by_id("login").click()  # set password
    time.sleep(10)

    print(check_project_exist(browser, "Rocket"))
    # click search


def check_project_exist(browser, prjName):
    import requests as rq
    url = r'https://agile.us.dell.com/Agile/PCMServlet?module=AutoCompleteHandler&opcode=completions&ajaxRequest=true&listId=291&classId=277075&refClsId=-1&attrId=2000008066&applyFiltering=false&append$USER=false&uiType=AutoComplete&condition=contains&format=text/plain&search=default&displayInactiveValues=true&query=' + prjName + r'&rnd=1455773506090&invalidate_session=false'
    jsStr = '''function httpGetSync(url){
                var xmlHttp = new XMLHttpRequest(); 
                xmlHttp.onreadystatechange = function() { 
	                if (xmlHttp.readyState == 4 && xmlHttp.status == 200) 
	                {
                        alert(xmlHttp.responseText);
	                } 
                };
                xmlHttp.open('GET', url, false); 
                xmlHttp.send(null);
                }'''

    return browser.execute_script(jsStr,url)

def HouseSearching():
    import requests
    import pandas
    url = r'https://sale.591.com.tw/home/search/list?type=2&&keywords=%E4%BF%A1%E7%BE%A9%E5%8D%80&shType=list&regionid=1&price=1500_2000&shape=2&pattern=3&area=30_40,20_30&timestamp=1518231863543'
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    res = requests.get(url, headers = headers)
    print(res.json())
    jd = res.json()

    df = pandas.DataFrame(jd['data']['house_list'])
    df = df[['is_newhouse', 'houseid', 'type', 'title', 'area', 'street_name', 'section_name']]
    print(df.head())
    #print(df.head())
    #df.to_excel("house_list.xlsx")

def missing_value():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame([['frank','M',np.nan], \
            ['mary', 'F', np.nan],\
            ['tom', 'M', 30],\
            ['jean', 'M', 55],])
    df.columns = ['name', 'gender', 'age']
    #print(df['age'].notnull())

    print(df.age.isnull().values.any())
    print(df.isnull().values.any())
    print(df.isnull().sum())
    print(df.isnull().sum().sum())
    print(df.dropna())

def issue_counter(filepath):
    import pandas
    pandas.read_excel(filepath)


#missing_value()
#Get_Agile_Data()
#check_project_exist('Rocket')