import tornado.web
import tornado.ioloop
from scraper.scraper import Scraper
from scraper.scrapeHandler import ScrapeHandler
from front_end.homePageHandler import HomePageHandler

scraper_obj = Scraper()

if __name__ == '__main__':
    # specify routes and their respective handlers in tornado application object.
    app = tornado.web.Application([
        (r"/", HomePageHandler),
        (r"/displayCountryDetails/", ScrapeHandler, dict(scraper_obj = scraper_obj)),
    ])

    """
        If any of the above "url routes" are 
        detected by tornado, it activates the
        corresponding micro web-service.
    """
    app.listen(8888)
    # start the app
    tornado.ioloop.IOLoop.current().start()