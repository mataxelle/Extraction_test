from bs4 import BeautifulSoup

with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')

page_title = soup.title
print(page_title.text)

h1_title = soup.find(id='title')
print(h1_title.text)

all_products = {}

products_list = soup.find('ul')

products = products_list.find_all('li')
for product in products:
   name = product.find('h2').string
   price_str = product.find('p', class_='price').string
   # 'â‚¬' is € sign
   price = float(price_str.split(" ")[1].strip("â‚¬"))
   price_dollar = price * 1.2
   description = product.find_all("p")[-1].string.strip('Description :')

   # name is used as a uniq cle
   all_products[name] = {
      'price': price,
      'price_dollar' : price_dollar,
      'description': description
   }

# Another solution with enumarate
"""
# Another solution with enumarate
for index, product in enumerate(products, start=1):
    name = product.find('h2').string
    price_str = product.find('p', class_='price').string
    price = float(price_str.split(" ")[1].strip("â‚¬"))
    description = product.find('p', class_='description').string
    
    all_products[f'{index}'] = {
        'name': name,
        'price': price,
        'description': description
    }
"""

print(all_products)