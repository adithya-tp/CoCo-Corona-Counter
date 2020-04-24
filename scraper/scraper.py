import json
import requests
from lxml import etree
from urllib.request import urlopen, Request

class Scraper():
    def scrape_count(self, country):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        url = "https://www.worldometers.info/coronavirus/country/{}/".format(country)
        response = urlopen(Request(url=url, headers=headers))
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        print(tree)
        parent_xpath = '//*[@id="maincounter-wrap"]/div/span/text()[1]'
        data_to_print = []
        for element in tree.xpath(parent_xpath):
            data_to_print.append(str(element).strip())
        return data_to_print
