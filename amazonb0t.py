!pip install selenium
from selenium import webdriver
import time
import re
from datetime import date
from pyfiglet import Figlet
from termcolor import colored
import sqlite3 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from prettytable import PrettyTable
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import itertools


class amzonBot:
    


    headers =  [  {
            'user-agent': 'Chrome/98.0.4758.102'
        } ,
        {
        'user-agent': 'Safari/537.36'
        }
            ,
        {
        'user-agent': 'Mozilla/5.0'
        }
        ]
    


    
    def __init__(self):
        
        self.headers =  [  {
            'user-agent': 'Chrome/98.0.4758.102'
        } ,
        {
        'user-agent': 'Safari/537.36'
        }
            ,
        {
        'user-agent': 'Mozilla/5.0'
        }
        ]
        
        self.driver = webdriver.Chrome('chromedriver.exe')
        
        self.url = 'https://www.amazon.in/'
    
    
    def start(i,entry):
        if entry == 'start':
        
            f = Figlet(font='speed')
            print((colored(f.renderText('Starting BOT .'), color="green")))

            print('\033[36m\033[1m What are we looking for Today \033[0m\033[0m')
        
        elif entry == 'scrap':
            print('\033[92m\033[1mHope Scrapping went well showd you results you want what can I do next \033[0m\033[0m')
        
        elif entry == 'productpg':
            print('\033[92m\033[1mI tried to get to best matching page , any thing else you want \033[0m\033[0m')
        
        elif entry == 'offer':
            print('\033[92m\033[1mLooks like today is having lots of cool deal Hope you found somthing helpfull there. what we r up to now  \033[0m\033[0m')
        
        elif entry == 'time':
            print('\033[92m\033[1mwell I love Dates and Datas  \033[0m\033[0m')
        elif entry == 'predict':
            print('\033[92m\033[1mwe predection scored Above 50 is considerable as per this modle other wise it will need some more feature Engeneered\033[0m\033[0m')
            
        a = input('\033[92m\033 :--- \033[0m\033[0m\n\n').lower()
        
        if re.search(' deal|deals|offers|offer',a.lower()):
            agbot.todaysdeal('a')
        elif re.search('buy|mobile|details|detail|add to| cart',a):
            name = input('enter brand name with model\n\n')
            agbot.product_details_pg(name)
        elif re.search('exit|end|sleep',a):
            agbot.exitmsg()
        elif re.search('date',a):
            agbot.date_time()
        elif re.search('scrape|scrap',a):
            b = input('enter product name with model\n\n')
            agbot.reqes('https://www.amazon.in/s?k={}&crid=3W2NRXBWWYRGW&sprefix=%2Caps%2C343&ref=nb_sb_noss'.format(b),'bot')
        elif re.search('predict',a):
            agbot.predict(key='start')
        elif re.search('info|help',a):
            agbot.info()
        else :
            print('try somthin else')
            agbot.start()
        
            
        
    def func(i):
        f = Figlet(font='poison')
        print((colored(f.renderText("GROUP - 4"), color="green")))

        t = PrettyTable(['S.No','function','Descreption'])
        t.add_row([1,'Scrape any Key','This function will scrape any Key word you Enter Example camera,heater,camera,etc..'])
        t.add_row([2,'Manual Insertion SQL Table','This function will allow you to Insert Values SQL Querys manually on terminal'])
        t.add_row([3,'Manual Creating SQL Table','This function will allow you to create SQL Querys manually on terminal'])
        t.add_row([4,'Project Demo','This function will Create Scraping and and database insertion automatically'])
        t.add_row([5,'Price Predection (Mobile)','This function will allow you to enter Features of Mobile and Will Predict Price'])
        print(t)
        
        a = input('Enter a function Key Or \033[36m\033[1m Start BOT \033[0m\033[0m ')
        if re.search('start|bot',a):
            agbot.start('start')
        elif a == '1':
            b = input('enter product you want to scrape \n\n')
            agbot.reqes('https://www.amazon.in/s?k={}&crid=3W2NRXBWWYRGW&sprefix=%2Caps%2C343&ref=nb_sb_noss'.format(b),'func')
        elif a == '5':
            print('\033[92m\033[1m PREDECTION WORKS ON BELOW SCHEMA \033[0m\033[0m')
            agbot.predict(key='func')
        else:
            print('try somthing Again')
            agbot.func()
        
            

    
    def reqes(self,url,catagory):    
        urls = url
        catagory = catagory
        x = np.random.randint(0,3)
        req = requests.get(url,headers=self.headers[x])
        try:
            print('enterd in try')
            req = requests.get(url,headers=self.headers[x])
        except:
            print('excepted')
            pass
        time.sleep(1)
        print("agent switched to :-")
        ab = req.text
        mb = str(req)
        print(type(mb))



        if re.search('503',mb) or re.search('To discuss automated access to Amazon data please contact api-services-support@amazon.com.',ab):
            print(mb)
            print('chainging agent proxy ---------- ')
            agbot.reqes(urls,catagory)
        else:
            soupe = BeautifulSoup(req.text,"html.parser")
            if catagory == 'bot' :
                return agbot.Scraper(soupe,'bot')
            elif catagory == 'func':
                return agbot.Scraper(soupe,'func')
        
        
    def Scraper(self,soup,key):
        
        Name = []
        Price = []
        Stars=[]
        
        Cost = []
        Brand_nam = []
        Type = []
        Stares = []


        name = soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')
        if name:
            for i in name:
                Name.append(i.contents[0])
            
            prices = soup.find_all('span',class_ ="a-price-whole")
            for i in prices:
                    x = 0
                    if x <= len(Name):
                        Price.append(i.contents[0])
                        x+=1
            strs = soup.find_all('span',class_='a-icon-alt')
            for i in strs:
                if re.search("[Up|.]$",i.contents[0]):
                    pass
                else:
                    Stars.append(i.contents[0])
            nest = [Name,Stars,Price]
            df = pd.DataFrame((_ for _ in itertools.zip_longest(*nest)), columns=['Name', 'Stars', 'Price'])
            print(df)

        elif soup.find_all('span',class_='a-size-base-plus a-color-base'):
            print('entered2')
            prices = soup.find_all('span',class_ ="a-price-whole")
            for i in prices:
                Cost.append(i.contents[0])

            Brand_names = soup.find_all('span',class_ = "a-size-base-plus a-color-base")
            for x in Brand_names:
                Brand_nam.append(x.contents[0])

            types = soup.find_all('span',class_ = "a-size-base-plus a-color-base a-text-normal")
            for z in types:
                Type.append(z.contents[0])

            strs = soup.find_all('span',class_='a-icon-alt')
            for i in strs:
                if re.search("[Up|.]$",i.contents[0]):
                    pass
                else:
                    Stares.append(i.contents[0])
                    
            nest = [Brand_Name,Type,Stares,Cost]
            df = pd.DataFrame((_ for _ in itertools.zip_longest(*nest)), columns=['Name', 'Type', 'Stars','Price'])
            print(df)
            
        else:
            name = soup.find_all('span',class_='a-size-base-plus a-color-base a-text-normal')
            for i in name:
                Name.append(i.contents[0])

            prices = soup.find_all('span',class_ ="a-price-whole")   
            for i in prices:
                x = 0
                if x<= len(Name):
                    Price.append(i.contents[0])
                x+=1

            strs = soup.find_all('span',class_='a-icon-alt')
            for i in strs:
                if re.search("[Up|.]$",i.contents[0]):
                    pass
                else:
                    Stars.append(i.contents[0])
            nest = [Name,Stars,Price]
            df = pd.DataFrame((_ for _ in itertools.zip_longest(*nest)), columns=['Name', 'Stars', 'Price'])
            print(df)
                    
        print(len(Price))
        print(len(Stars))
        print(len(Name))
        fram = pd
        if key == 'bot':
            agbot.start('scrap')
        elif key == 'func':
            agbot.func()
        
        
    def product_details_pg(self,model):
        self.driver = webdriver.Chrome('chromedriver.exe')
        
        a = self.driver.get(self.url)
        a
        print(a)
        time.sleep(2)
        self.driver.find_element_by_name("field-keywords").send_keys("'",model,"'")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
        try:
            self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a').click()
        except:
            self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a').click()
            
        agbot.start('productpg')
        
    def todaysdeal(self,deals):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get(self.url)
        self.driver.find_element_by_xpath('//*[@id="nav-xshop"]/a[4]').click()
        agbot.start('offer')
 
        
    def exitmsg(a):
        print('\033[36m\033[1m A M A Z O N   B O T   E X E T I N G . . . . \033[0m\033[0m \n')
        
        f = Figlet(font='larry3d')
        print((colored(f.renderText('Good bye.'), color="red")))
        
    
    def date_time(a):
        today = date.today()
        d2 = today.strftime("%b-%d-%Y")
        print(d2)
        f = Figlet(font='italic')
        print((colored(f.renderText(d2), color="green")))
        agbot.start('time')
        
    def predict(i,key):
        t = PrettyTable(['RAM','ROM','MobileSize','PrimaryCamera','SelfiCam','Battry'])
        print(t)
        
        ram,rom,scrnsiz,campri,selfcam,battry = input('enter features as per above SCHEMA ').split()
        df = pd.read_csv('mob.csv')
        df['Selfi_Cam']=df['Selfi_Cam'].fillna(0)
        df.drop(['Brand me'],axis=1,inplace=True)
        df = df.dropna()
        X = df.iloc[:,[6,2,4,5,1,3]]
        y = df.iloc[:,[-1]]

        df['Ratings'] = df['Ratings'].fillna(df['Ratings'].mean())
        df['RAM'] = df['RAM'].fillna(df['RAM'].mean())
        df['ROM'] = df['ROM'].fillna(df['ROM'].mean())
        df['Mobile_Size'] = df['Mobile_Size'].fillna(df['Mobile_Size'].mean())
        df['Selfi_Cam'] = df['Selfi_Cam'].fillna(df['Selfi_Cam'].mean())

        df['RAM'] = df['RAM'].astype('int64')
        df['ROM'] = df['ROM'].astype('int64')
        df['Selfi_Cam'] = df['Selfi_Cam'].astype('int64')


        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=15)
        reg = RandomForestRegressor()
        reg.fit(X_train,y_train)


        a = reg.predict([[ram,rom,scrnsiz,campri,selfcam,battry]])


        print("Testing Accuracy:",reg.score(X_test,y_test))
        time.sleep(5)
        print('start training ############')
        time.sleep(2)
        print('fetching data to model')
        print("Train Accuracy:",reg.score(X_train,y_train))
        print('\033[95m\033[1m Predicted Values as per model : --\033[0m''\033[0m',a)
        if key == 'func':
            agbot.func()
        elif key == 'start':
            agbot.start(entry='predict')

    def info(i):
        print('\033[95m\033[1mPRODUCT DETAILS PAGE :-- \033[0m\033[0m \n')
        print('\033[1m\t\t\t\t\t This function is automated using SElenium library to open amazon page and take user to detail page of inputed keywords mainly work on pages which is having html classes of one product per line the page is limited to mobile or electronic catagories \n  \033[0m :-- \n')
        print('\033[36m\033[1m NOTE :- function can only be ascess through bot with keyword like buy,details,add to ,cart \033[0m\033[0m\n\n\n')
        
        print('\033[95m\033[1m SCRAPER :-- \033[0m\033[0m\n')
        print('\033[1m\t\t\t\t\t This Function is main foucus of project it takes user arguments as input for amazon search field and retrive all data on that page and after converting it to nice dataframe show back to user which is understable,module used for this function is beatufull Soup and pandas for dataframe \033[0m \n')
        print('\033[36m\033[1m NOTE :- function can be ascess through bot or function menue with keyword like buy,details,add to ,cart \033[0m\033[0m\n')
        print('\033[91m\033[1m AMAZON always changes its ui and features so there is possiblities of errors which can be rectified by just changing single line in soup \033[0m\033[0m\n\n\n')
        
        print('\033[95m\033[1m Todays Deal :-- \033[0m\033[0m\n')
        print('\033[1m\t\t\t\t\t This is bot module which takes user argument and takes user to todays Deal section on Amazon where user can select deals and offer which ever user find interesting  \033[0m \n')
        print('\033[36m\033[1m NOTE :- function can be ascess through bot only with keyword like Offer,deals,todays offer \033[0m\033[0m\n')
        print('\033[91m\033[1m AMAZON always changes its User Interface so there is possiblities of  opening anather page which can be rectified by just changing single line in soup \033[0m\033[0m\n\n\n')

        print('\033[95m\033[1m DATE AND TIME :-- \033[0m\033[0m\n')
        print('\033[1m\t\t\t\t\t This is simple function which displays todays DATE in Graphity form \033[0m \n')
        print('\033[36m\033[1m NOTE :- function can be ascess through bot only with keyword like todays,date \033[0m\033[0m\n\n\n')        
        
        print('\033[95m\033[1m PRICE PREDECTION :-- \033[0m\033[0m\n')
        print('\033[1m\t\t\t\t\t This is Function contains SUPERVISED LEARNING for predecting price of product with user input of some co related features in this model we used Random Forest for predection AS other regresin models not Performing Well this Model Alread have Scraped Data file Attached From which it Takes Training and testing sets And Predicts Price . Still Tuning of some features Required on this Model\033[0m \n')
        print('\033[36m\033[1m NOTE :- function can be ascess through bot or function menue with keyword like Predict \033[0m\033[0m\n')
        print('\033[91m\033[1m Module Needs Some Tuning and Features Training if Accurasy Is below 40% above 60% is good & Considerable \033[0m\033[0m\n\n')
        
        print('\033[95m\033[1m SCRAPER :-- \033[0m\033[0m\n')
        print('\033[1m\t\t\t\t\t This Function is main foucus of project it takes user arguments as input for amazon search field and retrive all data on that page and after converting it to nice dataframe show back to user which is understable,module used for this function is beatufull Soup and pandas for dataframe \033[0m \n')
        print('\033[36m\033[1m NOTE :- function can be ascess through bot or function menue with keyword like buy,details,add to ,cart \033[0m\033[0m\n')
        print('\033[91m\033[1m AMAZON always changes its ui and features so there is possiblities of errors which can be rectified by just changing single line in soup \033[0m\033[0m')

        print('\033[91m\033[1m AMAZONE CHANGES ITS USER INTERFACES AND FEATURES ON CONSTINT BASIS SO SOME FUNCTIONS WILL NEED TO UPDATE WHENEVER SOMTHING CHANGES ON SITE  \033[0m\033[0m\n\n\n\n')
        
        f = Figlet(font='moscow')
        print((colored(f.renderText('Created BY :-- .'), color="blue")))
        print('\033[95m\033[1m\033[91m Mridul Chaturvdedi \033[0m\033[0m\033[0m')
        print('\033[95m\033[1m\033[91m Nainesh Bharambi \033[0m\033[0m\033[0m')
        print('\033[95m\033[1m\033[91m Nishant Sharma \033[0m\033[0m\033[0m')
        print('\033[95m\033[1m\033[91m Sami Khan \033[0m\033[0m\033[0m')

        
        agbot.start(entry='start')
        
    
agbot = amzonBot()
agbot.func()

# a = input('Enter a function Key Or \033[36m\033[1m Start BOT \033[0m\033[0m ')
# if re.search('start|bot',a):
#     agbot.start('start')
# elif a == '1':
#     Scraper('')
# time.sleep(5) short

