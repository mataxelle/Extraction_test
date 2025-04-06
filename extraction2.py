import requests
import csv
from bs4 import BeautifulSoup

def extracting(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find(class_='gem-c-cards')

def transforming(container, tag, class_name):
    # Direct reading with get_text(strip=True) to remove spaces
    return [el.get_text(strip=True) for el in container.find_all(tag, class_=class_name)]

def loading(data, headers, filename):
    # Support a wide range of characters with utf and newline
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def etl_pipeline():
    url = "https://www.gov.uk/"
    container = extracting(url)
    titles = transforming(container, 'a', 'govuk-link gem-c-cards__link gem-c-force-print-link-styles')
    descriptions = transforming(container, 'p', 'govuk-body gem-c-cards__description')
    data = list(zip(titles, descriptions))
    headers = ["Titles", "Descriptions"]
    loading(data, headers, 'gov_datas_bis.csv')

if __name__ == "__main__":
    etl_pipeline()
