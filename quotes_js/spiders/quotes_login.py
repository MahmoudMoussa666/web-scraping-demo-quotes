import scrapy
from scrapy.shell import inspect_response

class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes_login'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.xpath('//input[@type="hidden"]/@value').get()
        yield scrapy.FormRequest(response.url, formdata={'csrf_token': token, 'username': 'jkfldaslkf', 'password': 'fdsalkf'}, callback=self.parse_data)

    def parse_data(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        # inspect_response(spider=self, response=response)
        for quote in quotes:
            yield {
                'text': quote.xpath('.//span[@class="text"]/text()').get(),
                'author': quote.xpath('.//span/small/text()').get(),
                'tags': quote.xpath('.//div[@class="tags"]/a/text()').getall(),
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse_data)