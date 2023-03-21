from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 
from tqdm import tqdm
session = HTMLSession()
r = session.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree")
soup = BeautifulSoup(r.html.html, 'html.parser')
pages = soup.find('div',class_="_2MImiq").find("span")
number_of_pages = int(pages.text.split("of")[1].strip())
print(number_of_pages)
for i in tqdm(range(1,number_of_pages+1)):
    url = f"https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page={i}"
    r = session.get(url)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    with open(f"phones/{i}.html","w",encoding="utf-8") as f:
        f.write(soup.prettify())