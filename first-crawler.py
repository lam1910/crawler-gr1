import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.hanoicomputer.vn/tai-nghe/c246.html-1']

    def parse(self, response):
        for title in response.css('.p-info'):
            yield {'title': title.css('a::text').get()}

        next_page = response.css('.paging')
        link_to_follow = next_page.css('a::attr(href)').extract()
        for link in link_to_follow:
            yield response.follow(link, self.parse)


