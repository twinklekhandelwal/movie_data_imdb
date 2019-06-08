import requests 
import pprint
import json
import time
import random
from bs4 import BeautifulSoup 
import pathlib
URL = "https://www.imdb.com/india/top-rated-indian-movies/"
res = requests.get(URL)
soup = BeautifulSoup(res.text,"html.parser")
div = soup.find('div', class_='lister')
tbody = div.find('tbody', class_='lister-list')
trs = tbody.find_all('tr')
def scrape_top_list():
    dic_list = []
    i = 0
    for tr in trs: 
        dic = {}
        i = i + 1
        name = tr.find('td', class_= 'titleColumn').a.get_text()
        year = tr.find('td', class_= 'titleColumn').span.get_text()
        url_movies = tr.find('td', class_='titleColumn').a['href']
        link =  'https://www.imdb.com' + url_movies
        rate = tr.find('td', class_= 'ratingColumn imdbRating').strong.get_text()
        dic['year']= int(year[1:5])
        dic['rATE'] = float(rate)
        dic['POSTION'] = int(i)
        dic['name'] = str(name)
        dic['url']= str(link)
        # print (dic)
        dic_list.append(dic)
    return dic_list
top_movies = (scrape_top_list()) 
# pprint.pprint (top_movies)