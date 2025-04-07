import csv
from bs4 import BeautifulSoup

with open("produit.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')
   title = soup.title.string
   print(title)

produits = []
for table in soup.find_all('table'):
    for tr in table.find_all('tr')[1:]:
        td = tr.find_all('td')
        nom = td[0].get_text()
        description = td[1].get_text()
        prix = td[2].get_text()
        quantite = td[3].get_text()
        produit = {
            'nom': nom,
            'description': description,
            'prix': prix,
            'quantite': quantite
        }
        produits.append(produit)

taux_de_change = 0.8
for produit in produits:
    prix_dollar = produit['prix'].replace('$', '')
    prix_dollar = float(prix_dollar)

    prix_euro = prix_dollar * taux_de_change
    produit['prix'] = str(round(prix_euro, 2)) + '€'

print(produits)

with open(f'{title}.csv', mode='w', newline='') as file:
    fieldnames = ['nom', 'description', 'prix', 'quantite']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for produit in produits:
        writer.writerow(produit)