import requests
import csv
from bs4 import BeautifulSoup
import json
import re
import string
from datetime import datetime
from datetime import date
from StoreCrawl import storeData

# allCrawledLinksYet = ["https://canova-games.web.app", "https://www.wikipedia.org/", "https://google.com", "https://pt.wikipedia.org/wiki/Laranja"]

now = datetime.now()
today = date.today()
current_time = now.strftime("%H-%M-%S")

csvPath = 'Crawler\CrawlerLinks'+str(today)+'--'+current_time+'.csv'

csvFile = csv.writer(open(csvPath, 'w'))
csvFile.writerow(['From Link', "Gotten Links"])

with open('Crawler\LinksToCrawl.json') as file:
   pages = json.load(file)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    aTags = soup.find_all('a')
    links = list()
    for tag in aTags:
        if tag.get('href') != None or tag.get('href') != "#":
            links.append(tag.get('href'))

    cleanLinks = list()

    for link in links:
        if link != None and link:
            if link == "#":
                continue
            
            if link.startswith("https:") or link.startswith("http:"):
                cleanLinks.append(link)
            else:
                if link[0] == "/" and link[1] in list(string.ascii_letters):
                    cleanLinks.append(item+link)
                else:
                    if link[0] == "#":
                        cleanLinks.append(item+link)
                    else:
                        cleanLinks.append("https:"+link)
    
    csvFile.writerow([item, cleanLinks])

storeData(csvPath)