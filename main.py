import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/"
page = requests.get(url)

# Extracting the desired information with Beautiful Soup
soup = BeautifulSoup(page.content, 'html.parser')

# Extracting specific class
resultats = soup.find(class_='gem-c-cards')

# Extracting links and their titles
links_titles = resultats.find_all('a', class_='govuk-link gem-c-cards__link gem-c-force-print-link-styles')
for title in links_titles:
    print(title.text)