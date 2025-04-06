import requests
import csv
from bs4 import BeautifulSoup

def extracting():
    url = "https://www.gov.uk/"
    page = requests.get(url)
    # Extracting the desired information with Beautiful Soup
    soup = BeautifulSoup(page.content, 'html.parser')
    # Extracting specific class
    resultats = soup.find(class_='gem-c-cards')
    return resultats

def transforming(container, tag, class_name):
    # Extracts all texts matching a specific tag and class in a given container
    return [element.text for element in container.find_all(tag, class_=class_name)]

titles_info = transforming(extracting(), 'a', 'govuk-link gem-c-cards__link gem-c-force-print-link-styles')
descriptions_info = transforming(extracting(), 'p', 'govuk-body gem-c-cards__description')

headings = ["Titles", "Descriptions"]

def loading():
    with open('gov_datas.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(headings)
        writer.writerows(zip(titles_info, descriptions_info))

if __name__ == "__main__":        
    loading()