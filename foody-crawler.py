import scrapy

class foodySpider(scrapy.Spider):
    name = 'foodyspider'
    start_urls = ['https://www.foody.vn/ha-noi/food/cafe']

    def parse(self, response):
        for title in response.css("div.row-item:nth-child(2) > div:nth-child(2) > div:nth-child(1)"):
            yield {'title': title.css("resname::h2::a::attr(title)").extract()}

