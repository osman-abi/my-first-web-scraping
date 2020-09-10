import scrapy
from ..items import DemoItem

class ScrapeNitra(scrapy.Spider):
    name = "nitra"
    start_urls = [
        "https://nitra.az/"
    ]

    def parse(self, response):
        items = DemoItem()
        marka = response.css("div.markamodel::text").extract()
        qiymet = response.css("div.qiymet::text").extract()

        items['marka'] = marka
        items['qiymet'] = qiymet
        yield items

        next_page = response.css('a.page-link::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)