import scrapy


class QuotesTableSpider(scrapy.Spider):
    name = 'quotes_table'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/tableful']

    def parse(self, response):
        quotes = response.css('tr:nth-child(even)')[:-1]
        for quote in quotes:
            yield dict(
            text = quote.xpath('.//td/text()').get(),
            tags = quote.xpath('.//following-sibling::tr[1]/td/a/text()').getall()
            )
