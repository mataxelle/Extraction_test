import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.gov.uk/"
page = requests.get(url)

# Extracting the desired information with Beautiful Soup
soup = BeautifulSoup(page.content, 'html.parser')

# Extracting specific class
resultats = soup.find(class_='gem-c-cards')

titles_info = []
links_titles = resultats.find_all('a', class_='govuk-link gem-c-cards__link gem-c-force-print-link-styles')
for titles in links_titles:
    titles_info.append(titles.text)

descriptions_info = []
links_descriptions = resultats.find_all('p', class_='govuk-body gem-c-cards__description')
for descriptions in links_descriptions:
    descriptions_info.append(descriptions.text)

headings = ["Titles", "Descriptions"]

with open('gov_datas.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(headings)
    for titles, descriptions in zip(titles_info, descriptions_info):
        line = [titles, descriptions]
        writer.writerow(line)