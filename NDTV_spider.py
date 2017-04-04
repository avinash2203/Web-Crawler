from urllib import request
from bs4 import BeautifulSoup
import requests

fw = open('headlines.txt','w')
i=0

def trade_spider(max_pages):
    page=1
    i=0
    while(page<=max_pages):
        url = 'http://www.ndtv.com'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('a',{'class':'item-title'}):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
            #fw.write(href+"\n")
            i = i+1
            fw.write(str(i)+".) "+title+"\n")
            get_single(href)
        fw.close()
        page += 1


def get_single(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for item in soup.findAll('div',{'class':'lhs_highlights'}):
        for highlights in item.find_all('li'):
            print(highlights.string)
            if highlights.string:
                fw.write(highlights.string)
    fw.write("\n")
    fw.write("\n")
trade_spider(1)



