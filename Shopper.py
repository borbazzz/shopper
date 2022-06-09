import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import numpy as np
import json

# Pegar os dados HTML a partir da URL
url = "https://programada.shopper.com.br/shop-cn/alimentos/"

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)
time.sleep(5)  # in seconds
driver.find_element_by_xpath('/html/body/header/div/div/ul[1]/li[2]/a').click()
time.sleep(5)  # in seconds
driver.find_element_by_name("email").send_keys("borbaz@yahoo.com.br")
driver.find_element_by_name("senha").send_keys("Paranoid1026!" + Keys.RETURN)
time.sleep(10)  # in seconds
driver.find_element_by_xpath('/html/body/div[1]/div[4]/ul/li[3]/a/span[1]').click()
time.sleep(10)  # in seconds
element = driver.find_element_by_xpath('/html/body/div[1]/div[8]/div')
html_content = element.get_attribute('outerHTML')
#print(html_content)

# Parsear o conteúdo HTML com o BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
#alimentos = soup.find('div', class_='sc-jdzWJC jHtkqy')
driver.quit()
#print(alimentos)

#convert output to new array, check length
array = np.asarray(soup,dtype=object)
#print(array)

#convert new array to dataframe
df = pd.DataFrame(array[0,1])

#acucar_e_adocantes = df
acucar_e_adocantes = (df[:1])

print(acucar_e_adocantes)

#export data
df.to_csv('/Users/rodrigo-borba/desktop/board_members.csv', sep=';')


#print(type(alimentos))

#alimentos = soup.findAll("div", class_="sc-cZbDLb eFiuxn")

#print(soup)

# Estruturar conteúdo em um Data Frame - Pandas

#df_full = pd.read_html(str(alimentos))[0]

#print(df_full)

############################################

#headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

#site = requests.get(URL, headers=headers)

