import json
import os
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from tqdm import tqdm
from multiprocessing import Pool


session = HTMLSession()
def extract_html(obj):
    phone_id = obj["id"]
    r = session.get(obj["review_url"])
    soup = BeautifulSoup(r.html.html, 'html.parser')
    pages = soup.find('div',class_="_2MImiq").find("span")
    number_of_pages = int(pages.text.split("of")[1].strip())
    print(f"Number of pages: {number_of_pages} for {obj['name']} ({obj['id']})")
    for i in range(1,number_of_pages+1):
        url = f"{obj['review_url']}&page={i}"
        r = session.get(url)
        soup = BeautifulSoup(r.html.html, 'html.parser')
        with open(f"reviews/{obj['id']}_{i}.html","w",encoding="utf-8") as f:
            f.write(soup.prettify())

if __name__=="__main__":
    with open("data.json") as f:
        data = json.load(f)
    print(len(data))
    with Pool(10) as p:
        p.map(extract_html, data)