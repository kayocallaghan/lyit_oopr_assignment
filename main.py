# This is a simple Python script to scrape and parse a webpage

import requests

if __name__ == "__main__":

    apache_page = requests.get("http://192.168.0.199/")
    open('apachescrape.html', 'wb').write(apache_page.content)
