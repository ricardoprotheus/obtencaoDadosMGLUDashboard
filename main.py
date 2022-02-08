import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Abrir o url do site
def abrirURL(url):
    option = Options()
    option.headless = True
    driver = webdriver.Chrome(options=option)  # executar em segundo plano
    driver.get(url)
    time.sleep(3)  # esperar o site abrir
    print(type(driver))
    return driver

#salvar arquivo em csv
def salvarCsv(arquivo, name):
    soup = BeautifulSoup(arquivo, 'html.parser')
    table = soup.find(name='table')
    data_frame = pd.read_html(str(table))[0]
    data_frame.to_csv(f'{name}.csv')

# https://br.financas.yahoo.com/quote/MGLU3.SA/financials?p=MGLU3.SA
urlCotacoes = "https://br.investing.com/equities/magaz-luiza-on-nm-historical-data"
urlFundamentus = "https://www.infomoney.com.br/cotacoes/magazine-luiza-mglu3/"
urlFundamentus2 = "https://www.infomoney.com.br/cotacoes/magazine-luiza-mglu3/"

# Cotações MGLU
driver = abrirURL(urlCotacoes)
element = driver.find_element(By.XPATH, "//*[@id='curr_table']")
html_content = element.get_attribute('outerHTML')
salvarCsv(html_content, 'cotacoesMGLU')

# Fundamentus 1
driver = abrirURL(urlFundamentus)
element = driver.find_element(By.XPATH, '//*[@id="header-quotes"]/div[2]/div[1]/table[2]')
html_content = element.get_attribute('outerHTML')
salvarCsv(html_content,'fundamentusMGLU')

#Fundamentus 2
driver = abrirURL(urlFundamentus2)
element = driver.find_element(By.XPATH,'//*[@id="header-quotes"]/div[2]/div[1]/table[1]')
html_content = element.get_attribute('outerHTML')
salvarCsv(html_content, 'fundamentus2MGLU')