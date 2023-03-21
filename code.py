import os
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from multiprocessing import Pool
number = 0

def get_details(soup):
    link = soup.find('a')
    review_url = ("https://www.flipkart.com"+link.get('href')).replace("/p/", "/product-reviews/")
    name = soup.find("div",class_="_4rR01T").text.strip()
    rating = float(soup.find("div",class_="_3LWZlK").text)
    price = soup.find("div",class_="_30jeq3").text.strip()[1:]
    obj = {
        "name": name,
        "rating": rating,
        "price": price,
        "review_url": review_url
    }
    return obj

def process_file(fname):
    with open(f"phones/{fname}","r",encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    phones = soup.find_all('div',class_="_2kHMtA")
    phone_details = []
    for phone in phones:
        try:
            details = get_details(phone)
            phone_details.append(details)
        except:
            pass
    print(f"Done with {fname}")
    return phone_details
if __name__=="__main__":
    phone_details = []
    with Pool(10) as p:
        phone_details = p.map(process_file,os.listdir("phones"))
    phone_details = [item for sublist in phone_details for item in sublist]
    with open("phone_details.json","w",encoding="utf-8") as f:
        json.dump(phone_details,f,indent=4)