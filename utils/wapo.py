import os 
import glob 
import requests 

from bs4 import BeautifulSoup 
from readability.readability import Document 


# Base Washington Post URL
WAPO_URL = "https://wapo.st/"
DATA = os.path.join(os.path.dirname(__file__), "..", "data", "wapo")


def fetch_wapo(sid):
    url = WAPO_URL + sid 
    res = requests.get(url)
    return res.text 


def save_wapo(sid, category="politics"):
    dpath = os.path.join(DATA, category)
    if not os.path.exists(dpath):
        os.makedirs(dpath)
    
    path = os.path.join(dpath, sid + ".html")
    with open(path, 'w') as f:
        f.write(fetch_wapo(sid)) 


def load_wapo(sid, category="*", extract=True):
    path = os.path.join(DATA, category, sid+".html") 
    paths = glob.glob(path)

    if len(paths) == 0:
        raise ValueError("could not find {} in {}".format(sid, category))

    with open(paths[0], 'r') as f:
        data = f.read()

    if extract:
        return extract_html_text(data)
    return data 


def extract_html_text(html):
    article = Document(html).summary() 
    soup = BeautifulSoup(article, 'lxml')
    return soup.get_text()
