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
        'body': wine_details
    }


def get_wine_details(url: str) -> dict:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    degustation_element = soup.find(
        "div", {"class": "product attribute degustation"}).find("div", {"class": "value"})

    degu_notes = degustation_element.text.strip()
    return degu_notes


def main(args):
    url = args[0]
    print(get_wine_details(url))


if __name__ == "__main__":
    main(sys.argv[1:])
