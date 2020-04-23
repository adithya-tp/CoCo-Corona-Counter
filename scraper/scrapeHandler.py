import tornado.web
from tornado.escape import json_decode
import pprint
import scraper
import json

"""
    When torado detects a url route /displayCountryDetails/
    then the following handler is invoked. This handler is 
    only called when the button in index.html is clicked. The 
    jquery function in index.html passes in the "country name"
    into this handler, in the form of a json object.
"""
class ScrapeHandler(tornado.web.RequestHandler):
    def initialize(self, scraper_obj):
        self.scraper = scraper_obj
        self.counts = []
    
    def post(self):
        # Decode post request body passed in from the jQuery function
        json_obj = json_decode(self.request.body)
        print('Post data received')

        country = ""
        # Get the country from the json_object
        for key in list(json_obj.keys()):
            print('key: %s , value: %s' % (key, json_obj[key]))
            country = json_obj[key]
        
        # Get the "corona case" count for the give country.
        self.counts = self.scraper.scrape_count(country)

        # Build up the response json.
        response_to_send = {}
        try:
            response_to_send['total'] = str(self.counts[0])
            response_to_send['death'] = str(self.counts[1])
            response_to_send['recovered'] = str(self.counts[2])
        # If you don't find the country, set all counts to "Page not found".
        except:
            response_to_send['total'] = "Page not found"
            response_to_send['death'] = "Page not found"
            response_to_send['recovered'] = "Page not found"


        print('Response to return')

        pprint.pprint(response_to_send)

        # Dump the json object to be returned to the jQuery.
        self.write(json.dumps(response_to_send))
