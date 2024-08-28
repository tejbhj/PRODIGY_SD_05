import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

products = []
for item in soup.find_all('article', class_='product_pod'):
    name = item.find('h3').find('a')['title']
    price = item.find('p', class_='price_color').text.strip()
    products.append([name, price])

with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price'])
    writer.writerows(products)
