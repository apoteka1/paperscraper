import json
import pprint
import logging
from bs4 import BeautifulSoup
from bs4 import SoupStrainer as strainer
import requests
import re
import asyncio
import time

search_term = 'truss'
search_term_re = r'\b(%s)\b' % search_term


async def main():
    sites = ["https://www.theguardian.com/uk",
             "https://www.bbc.co.uk/news", "https://www.thesun.co.uk/"]

    counts = {}

    async def scrape(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        mentions = soup.find_all(string=re.compile(
            search_term_re, re.IGNORECASE))
        site_name = url.split('www.')[1].split('.')[0]
        print(len(mentions))

        # counts[site_name] = len(mentions)

    coros = [scrape(s) for s in sites]

start = time.time()
asyncio.run(main())
print("gather", time.time() - start)

