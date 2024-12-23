from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

URL = 'https://www.tokopedia.com/search?'
params = {'q': 'bagiak%20khas%20banyuwangi'}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

driver = webdriver.Chrome()
fullURL = f"{URL}&q={params['q']}"
driver.get(fullURL)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-5wh65g')))
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data = soup.find_all('div', {'class': 'css-5wh65g'})
for i in range(len(data)):
    nama = data[i].find('div', {'class': '_6+OpBPVGAgqnmycna+bWIw=='})
    harga = data[i].find('div', {'class': '_67d6E1xDKIzw+i2D2L0tjw=='})
    penjual = data[i].find('span', {'class': 'T0rpy-LEwYNQifsgB-3SQw=='})
    if nama and harga and penjual:
        print("Nama produk: " + nama.text.strip())
        print("Harga: " + harga.text.strip())
        print("Penjual: " + penjual.text.strip(), "\n")

driver.quit()
