from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

jogo = input('Qual jogo deseja pesquisar: ')

url = 'https://store.steampowered.com/'

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(url)

button = browser.find_element_by_xpath('//*[@id="store_nav_search_term"]').send_keys(jogo)

button2 = browser.find_element_by_xpath('//*[@id="store_search_link"]/img')

button2.click()

time.sleep(10)

browser.close()





# pip install selenium
# pip install webdriver-manager
#pip install time