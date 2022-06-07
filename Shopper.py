import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
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
time.sleep(20)  # in seconds
driver.find_element_by_xpath('/html/body/div[1]/div[4]/ul/li[3]/a/span[1]').click()
time.sleep(20)  # in seconds
element = driver.find_element_by_xpath('/html/body/div[1]/div[8]/div')
html_content = element.get_attribute('outerHTML')

# Parsear o conteúdo HTML com o BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
driver.quit()
alimentos = soup.findAll('p', {'class': 'sc-DJmSI kXVaHC'})
print(alimentos)

# Estruturar conteúdo em um Data Frame - Pandas

#df_full = pd.read_html(alimentos)

#print(df_full)

