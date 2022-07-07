import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes_js'
    allowed_domains = ['toscrape.com']
    
    def start_requests(self):
        url = 'https://quotes.toscrape.com/js'
        yield scrapy.Request(url, meta={
            'playwright':True
        })

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'text': quote.xpath('.//span/text()').get(),
                'author': quote.xpath('.//span/small/text()').get(),
                'tags': quote.xpath('.//div/a/text()').getall()
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, meta={'playwright':True})