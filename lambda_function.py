import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    body = event['body']
    content = json.loads(body)

    url = content['url']
    # URL = "https://www.bindella.ch/weinshop/villa-antinori-riserva-chianti-classico-docg-riserva-antinori-nel-chianti-classico1917"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    degustation_element = soup.find("div", {"class": "product attribute degustation"}).find("div", {"class": "value"})

    degu_notes = degustation_element.text.strip()

    return {
        'statusCode': 200,
        # 'body': json.dumps(event['body'])
        # 'body': content['url']
        'body': degu_notes
    }
