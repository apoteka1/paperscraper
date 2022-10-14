
from bs4 import BeautifulSoup
from bs4 import SoupStrainer as strainer
import requests
import re
import asyncio
import time

search_term = 'truss'
search_term_re = r'\b(%s)\b' % search_term

sites = ["https://www.theguardian.com/uk",
         "https://www.bbc.co.uk/news", "https://www.thesun.co.uk/", "https://www.theguardian.com/uk",
         "https://www.bbc.co.uk/news", "https://www.thesun.co.uk/", "https://www.theguardian.com/uk",
         "https://www.bbc.co.uk/news", "https://www.thesun.co.uk/", "https://www.theguardian.com/uk",
         "https://www.bbc.co.uk/news", "https://www.thesun.co.uk/"]

counts = {}


def sync_scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    mentions = soup.find_all(string=re.compile(
        search_term_re, re.IGNORECASE))
    site_name = url.split('www.')[1].split('.')[0]
    print(len(mentions))


async def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    mentions = soup.find_all(string=re.compile(
        search_term_re, re.IGNORECASE))
    site_name = url.split('www.')[1].split('.')[0]
    print(len(mentions))
    # counts[site_name] = len(mentions)


async def main():
    await asyncio.gather(*[scrape(s) for s in sites])


def list_comp():
    for s in sites:
        sync_scrape(s)


start = time.time()
asyncio.run(main())
print("gather", time.time() - start)


start = time.time()
list_comp()
print("listcomp", time.time() - start)


# def lambda_handler(event, context):
#     logger.debug('Hello world')
#     logger.debug(f"Event {json.dumps(event)}")
#     pprint.pprint(context)
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }
