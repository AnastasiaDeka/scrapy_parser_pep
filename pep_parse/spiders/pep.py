import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.css(
            '#index-by-category tbody tr a::attr(href)'
        ).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number = response.css('h1.page-title::text').re_first(r'PEP (\d+)')
        name = response.css('h1.page-title::text').re_first(r'PEP \d+ – (.+)')
        status = response.css('dd abbr::text').get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
