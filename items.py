# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExpediaItem(scrapy.Item):
    # define the fields for your item here like:
    Flight_number = scrapy.Field()
    Origin = scrapy.Field()
    Destination = scrapy.Field()
    Departure_time = scrapy.Field()
    Arrival_time = scrapy.Field()
    comfort_title = scrapy.Field()
    price = scrapy.Field()