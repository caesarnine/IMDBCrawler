# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ImdbcrawlItem(Item):
    title = Field()
    year = Field()
    rating = Field()
    votes = Field()
    runtime = Field()
    genres = Field()
