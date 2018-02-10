def Get_Agile_Data():
    from selenium import webdriver
    import time
    chrome_path = r'C:\selenium\chromedriver.exe'
    web = webdriver.Chrome(chrome_path)

    web.get('https://agile.us.dell.com/Agile/default/login-cms.jsp')
    web.set_window_position(0,0)
    web.set_window_size(700,700)
    time.sleep(5)

    web.find_element_by_id('j_username').send_keys('yoyo_z_zhang@wistron.com') #set account
    web.find_element_by_id("j_password").send_keys('Linna2041') #set password
    web.find_element_by_id("login").click()  # set password
    time.sleep(5)

    # web.close()

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
Get_Agile_Data()
