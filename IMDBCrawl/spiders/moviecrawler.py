from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from IMDBCrawl.items import ImdbcrawlItem
from scrapy.http import Request


class MySpider(CrawlSpider):
    name = "IMDBCrawler"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["http://www.imdb.com/search/title?at=0&sort=num_votes,desc&start=1&title_type=feature&year=1950,2012"]

    rules = (
    Rule(SgmlLinkExtractor(restrict_xpaths=("(//span[@class='pagination'])[2]/a[last()]"),unique=True), follow = True, callback='parse_start_url'),
    )        

    def parse_start_url(self, response):
        hxs = HtmlXPathSelector(response)
        even_titles = hxs.select('//tr[@class="even detailed"]')
        odd_titles = hxs.select('//tr[@class="odd detailed"]')
        items = []
        
        for titles in even_titles:
            item = ImdbcrawlItem()
            item ['title'] = titles.select('td[@class="title"]/a/text()').extract()
            item ['year'] = titles.select('td[@class="title"]/span[@class="year_type"]/text()').extract()
            item ['rating'] = titles.select('td[@class="title"]/div[@class="user_rating"]/div[@class="rating rating-list"]/span[@class="rating-rating"]/span[@class="value"]/text()').extract()
            item ['votes'] = titles.select('td[@class="sort_col"]/text()').extract()
            item ['runtime'] = titles.select('td[@class="title"]/span[@class="runtime"]/text()').extract()
            item ['genres'] = titles.select('td[@class="title"]/span[@class="genre"]/a/text()').extract()
            items.append(item)
        
        for titles in odd_titles:
            item = ImdbcrawlItem()
            item ['title'] = titles.select('td[@class="title"]/a/text()').extract()
            item ['year'] = titles.select('td[@class="title"]/span[@class="year_type"]/text()').extract()
            item ['rating'] = titles.select('td[@class="title"]/div[@class="user_rating"]/div[@class="rating rating-list"]/span[@class="rating-rating"]/span[@class="value"]/text()').extract()
            item ['votes'] = titles.select('td[@class="sort_col"]/text()').extract()
            item ['runtime'] = titles.select('td[@class="title"]/span[@class="runtime"]/text()').extract()
            item ['genres'] = titles.select('td[@class="title"]/span[@class="genre"]/a/text()').extract()
            items.append(item)
            
        return(items)
