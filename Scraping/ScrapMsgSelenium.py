# Programa para realizar scraping do Likedin de mensagens a partir de uma hashtag
# Pesquisa feita sem usuário logado

# Importar bibliotecas
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

#instalando o driver mais atual correspondente ao Chrome, instanciando e abrindo o navegador
# servico = Service(ChromeDriverManager().install())
servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)
navegador.get("https://www.google.com")
time.sleep(10)
#################### Scraping ##############################
### https://selenium-python.readthedocs.io/



# Listando as páginas
textoPesquisa = navegador.find_element('xpath','//*[@id="APjFqb"]')
textoPesquisa.send_keys( '"#escala6x1" site:linkedin.com')
time.sleep(10)
botaoPesquisar = navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
botaoPesquisar.click()
print('teste')

#//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/div/div[2]/div[1]/div