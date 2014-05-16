IMDBCrawler
===========

A web crawler I created to learn how to use Scrapy. It craws the top movies list, and scrapes information about each movie, such as name, rating, genres, and more. The start page is:

http://www.imdb.com/search/title?at=0&sort=num_votes,desc&start=1&title_type=feature&year=1950,2012

To run it, run:

```
scrapy -o movies.csv -t csv
```

This will start the Spider, and push the output into a csv file and format it as a CSV.
