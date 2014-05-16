# Scrapy settings for IMDBCrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'IMDBCrawl'

SPIDER_MODULES = ['IMDBCrawl.spiders']
NEWSPIDER_MODULE = 'IMDBCrawl.spiders'
#DUPEFILTER_CLASS = 'IMDBCrawl.custom_filters.CustomFilter'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'IMDBCrawl (+http://www.yourdomain.com)'
