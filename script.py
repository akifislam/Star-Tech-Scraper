from bs4 import BeautifulSoup
import requests

#Connection Setup !
source_link = requests.get("https://www.startech.com.bd/product/search?search=Macbook&category_id=0").text
soup = BeautifulSoup(source_link, "lxml")



main_row = soup.find('div', class_="search-products margin-top product-listing m-t-15")
counter = 1
price_list = []

for data in main_row.findAll('div',class_='product-info') :
    product_name = data.find('h4',class_='product-name').find('a').text
    product_link = data.find('h4',class_='product-name').find('a')['href']
    description = data.find('div',class_='descriptions').find('li').text
    price = data.find('div',class_='price').find('span').text
    print(f"---{counter}---")
    counter = counter + 1
    print(product_link)
    print(product_name)
    print(description)
    print(price)
    print()
    print()



source_link2 = requests.get("https://www.startech.com.bd/product/search?&search=Macbook&category_id=0&page=2").text
soup2 = BeautifulSoup(source_link2, "lxml")

main_row2 = soup.find('div', class_="search-products margin-top product-listing m-t-15")
for data in main_row2.findAll('div',class_='product-info') :
    product_name = data.find('h4',class_='product-name').find('a').text
    product_link = data.find('h4',class_='product-name').find('a')['href']
    description = data.find('div',class_='descriptions').find('li').text
    price = data.find('div',class_='price').find('span').text
    print(f"---{counter}---")
    counter = counter + 1
    print(product_link)
    print(product_name)
    print(description)
    print(price)
    print()
    print()
