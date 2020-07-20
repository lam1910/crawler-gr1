import scrapy


class travelBlagCrawler(scrapy.Spider):
    name = 'normadspider'
    start_urls = ['https://www.nomadicmatt.com/travel-guides/vietnam-travel-tips/']

    xpath_to_content = '/html/body/div[1]/div[2]/div/main/article/div'

    def parse(self, response):
        for title in response.xpath(self.xpath_to_content):
            yield {'title': title.xpath("//one-fifth").extract()}