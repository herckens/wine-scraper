import sys
import json
import requests
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    body = event['body']
    request_content = json.loads(body)
    url = request_content['url']

    wine_details = get_wine_details(url)

    return {
        'statusCode': 200,
        'body': json.dumps(wine_details, ensure_ascii=False)
    }


def get_wine_details(url: str) -> dict:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    degu_notes = extract_degu_notes(soup)
    vinification = extract_vinification(soup)
    return {
        "degu_notes": degu_notes,
        "vinification": vinification
    }


def extract_degu_notes(soup):
    degustation_element = soup.find(
        "div", {"class": "product attribute degustation"}).find("div", {"class": "value"})
    degu_notes = degustation_element.text.strip()
    return degu_notes


def extract_vinification(soup):
    vinification_element = soup.find(
        "div", {"class": "product attribute vinification"}).find("div", {"class": "value"})
    vinification = vinification_element.text.strip()
    return vinification


def main(args):
    url = args[0]
    wine_details = get_wine_details(url)
    print(json.dumps(wine_details, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1:])
