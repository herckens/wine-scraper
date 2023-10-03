import requests
from bs4 import BeautifulSoup

URL = "https://www.bindella.ch/weinshop/villa-antinori-riserva-chianti-classico-docg-riserva-antinori-nel-chianti-classico1917"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
degustation_element = soup.find("div", {"class": "product attribute degustation"}).find("div", {"class": "value"})

degu_notes = degustation_element.text.strip()
print(degu_notes)
