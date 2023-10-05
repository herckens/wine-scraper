import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    url = event['url']
    # URL = "https://www.bindella.ch/weinshop/villa-antinori-riserva-chianti-classico-docg-riserva-antinori-nel-chianti-classico1917"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    degustation_element = soup.find("div", {"class": "product attribute degustation"}).find("div", {"class": "value"})

    degu_notes = degustation_element.text.strip()

    return {
        'statusCode': 200,
        'body': degu_notes
    }
