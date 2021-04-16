from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

driver.get('https://www.1mg.com/drugs-all-medicines')

medicine = pd.DataFrame({'Name':[''], 'Unit':[''], 'Composition':[''], 'Link':['']})

while True:

    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_='style__product-card___1gbex style__card___3eL67 style__raised___3MFEA style__white-bg___10nDR style__overflow-hidden___2maTX')

    for post in postings:
        name = post.find('div', class_='style__font-bold___1k9Dl style__font-14px___YZZrf style__flex-row___2AKyf style__space-between___2mbvn style__padding-bottom-5px___2NrDR').text
        unit = post.find('div', class_='style__flex-column___1zNVy style__font-12px___2ru_e').text
        compo = post.find('div', class_='style__font-12px___2ru_e style__product-content___5PFBW style__display-inline-block___2y7gd').text
        link = post.find('a', class_='button-text style__flex-row___2AKyf style__flex-1___A_qoj style__product-name___HASYw').get('href')
        link_full = 'https://www.1mg.com'+link
        
    
        medicine = medicine.append({'Name': name, 'Unit': unit, 'Composition': compo, 'Link': link_full}, ignore_index=True)
    
    try:
        button = soup.find('a', class_='button-text link-next').get('href')
        driver.get('https://www.1mg.com/'+button)
    except:
        pass

medicine.to_csv('1mg_med1.csv')


        


