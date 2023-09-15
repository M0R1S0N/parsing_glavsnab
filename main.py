import requests
from bs4 import BeautifulSoup
import pandas as pd 


url='https://glavsnab.com/catalog/elektrotekhnicheskie_izdeliya/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')



data = []

for p in range(1, 27):
    print(p)
    
    url = f'https://glavsnab.com/catalog/elektrotekhnicheskie_izdeliya/?count=30&PAGEN_1={p}&SIZEN_1=30'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    
    
    products = soup.find_all('div', class_='product-item-container')

    for product in products:
        sku = product.find('div', class_='code_t').text
        link = 'https://glavsnab.com'+soup.find('div', class_='catalog_list_item').find('a').get('href')
        name = product.find('div', class_='catalog_list_item_title').text
        price = product.find('div', class_='price').text
        len_price = len(price)
        price = price[0:len_price-3]
        data.append([sku, link, name, int(price)])

header = ['Код ', 'Ссылка ', 'Название ', 'Цена']
df = pd.DataFrame(data, columns=header)
df.to_csv('C:/Users/ryazantsev/Desktop/glavsnab.csv', sep=';', encoding='utf8')





