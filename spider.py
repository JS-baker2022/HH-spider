import requests
from bs4 import BeautifulSoup

#url = "https://hh.ru/search/vacancy?text=Fullstack&from=suggest_post&area=1&hhtmFrom=main&hhtmFromLabel=vacancy_search_line"

#headers = {
    #"Accept": "*/*",
    #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
#}
#req = requests.get(url, headers=headers)

#src = req.text
#print(src)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)