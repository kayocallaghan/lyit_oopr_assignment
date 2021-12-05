# This is a simple Python script to scrape and parse a webpage

import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":

    # scraping the default Apache page
    apache_page = requests.get("http://192.168.0.199/")
    open('apachescrape.html', 'wb').write(apache_page.content)

    with open("apachescrape.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

        # run through list of tags to find and print all present on scraped page
        headings = ["h1", "h2", "h3", "h4", "h5", "h6"]
        for tag in soup.find_all(headings):
            print(tag)
            # there are no h1, h2 etc. tags on the apache page so there is no output here

        # find number of instances of Apache2
        result = soup.find_all(string=re.compile("Apache2"))
        print(len(result))

        # find the number of a tags on the page
        hyperlinks_on_page = soup.find_all("a")
        print(len(hyperlinks_on_page))



