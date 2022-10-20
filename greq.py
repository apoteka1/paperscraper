from itertools import count
from bs4 import BeautifulSoup
import grequests as greq
import re


def get_counts(search_term):
    search_term_re = r'\b(%s)\b' % search_term
    sites = [("The Guardian", "https://www.theguardian.com/uk"), ("Daily Mail", "https://www.dailymail.co.uk/home/index.html"),
             ("BBC", "https://www.bbc.co.uk/news"), ("The Sun", "https://www.thesun.co.uk/")]

    counts = {}
    requests = (greq.get(site[1]) for site in sites)
    responses = greq.map(requests)

    for i, r in enumerate(responses):
        soup = BeautifulSoup(r.content, 'html.parser')
        mentions = soup.find_all(string=re.compile(
            search_term_re, re.IGNORECASE))
        site_name = sites[i][0]
        counts[site_name] = len(mentions)

    return counts


