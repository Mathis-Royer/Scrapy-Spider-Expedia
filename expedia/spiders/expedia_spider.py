import scrapy
from scrapy_playwright.page import PageMethod
from ..items import ExpediaItem
import requests
from urllib.parse import urlencode
from scrapy_playwright.page import PageMethod

API_KEY = 'ff5769d6316928b654abf71b7a2cae07'

def get_scraperapi_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url

class expediaSpider (scrapy.Spider):
    name = 'expedia_spider'

    def start_requests(self) :

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36'} #nécessaire de l'ajouter lorsque le site a détecté le scraping et a bloqué le User-agent par défaut de scrapy
        url_aller ='https://www.expedia.fr/Flights-Search?leg1=from:'+self.origin+',to:'+self.destination+',departure:'+self.depart_date+'TANYT&mode=search&options=carrier:*,cabinclass:,maxhops:1,nopenalty:N&pageId=0&passengers=adults:1,children:0,infantinlap:N&trip=oneway'
        url_retour ='https://www.expedia.fr/Flights-Search?leg1=from:'+self.destination+',to:'+self.origin+',departure:'+self.return_date+'TANYT&mode=search&options=carrier:*,cabinclass:,maxhops:1,nopenalty:N&pageId=0&passengers=adults:1,children:0,infantinlap:N&trip=oneway'
        urls = [url_aller,url_retour]
        meta=dict(playwright = True,                #utilisation de scrapy.playright pour la gestion des pages utilisant du javascript
                  playwright_include_page = True,
                  playwright_page_method = [
                    PageMethod("wait_for_selector", "span.uitk-lockup-price")
                  ],
                  )
        
        for url in urls:
            yield scrapy.Request(url=get_scraperapi_url(url), meta=meta, callback=self.parse_flights)

        # yield scrapy.Request(url_aller, meta=meta, headers = headers,callback=self.parse_flights)
        # yield scrapy.Request(url_retour, meta=meta, headers = headers,callback=self.parse_flights)



    async def parse_flights(self, response):
        page = response.meta["playwright_page"]
        await page.screenshot(path="screenshot.png")
        await page.close()

        expediaItem = ExpediaItem()
        offers = response.css('div.uitk-layout-flex.uitk-layout-flex-justify-content-space-between.uitk-layout-flex-gap-six.uitk-layout-flex-flex-wrap-nowrap.uitk-layout-grid-item')
        
        for offer in offers:
            expediaItem['Flight_number'] = ""   #numéro de vol non disponible à ma connaissance sur expédia
            expediaItem['Origin'] = offer.css('div.uitk-text.truncate.uitk-type-200.uitk-text-emphasis-theme.uitk-spacing.uitk-spacing-margin-blockstart-one::text').get()
            expediaItem['Origin'] = expediaItem['Origin'][expediaItem['Origin'].index("(")+1:expediaItem['Origin'].index("(")+4]
            expediaItem['Destination'] = offer.css('div.uitk-text.truncate.uitk-type-200.uitk-text-emphasis-theme.uitk-spacing.uitk-spacing-margin-blockstart-one::text').get()
            expediaItem['Destination'] = expediaItem['Destination'][expediaItem['Destination'].index("(", expediaItem['Destination'].index("(")+4)+1:expediaItem['Destination'].index("(", expediaItem['Destination'].index("(")+4)+4]
            expediaItem['Departure_time'] = offer.css('span.uitk-text.uitk-type-400.uitk-type-bold.uitk-text-emphasis-theme::text').get()
            expediaItem['Departure_time'] = expediaItem['Departure_time'][:7]
            expediaItem['Arrival_time'] = offer.css('span.uitk-text.uitk-type-400.uitk-type-bold.uitk-text-emphasis-theme::text').get()
            expediaItem['Arrival_time'] = expediaItem['Arrival_time'][10:]
            expediaItem['comfort_title'] = ""   #difficulté pour obtenir la classe car interaction avec des button et fonctions javascripts
            expediaItem['price'] = offer.css('span.uitk-lockup-price::text').get()

            yield expediaItem