import scrapy

class githubRepoSpider(scrapy.Spider):
    name = 'githubrepospider'
    start_urls = ['https://github.com/vietanhdev?tab=repositories']

    def parse(self, response):
        base_url = 'https://www.github.com'
        for i in range(1,31):
            title = response.css('li.col-12:nth-child({}) > div:nth-child(1) > '
                                 'div:nth-child(1) > h3:nth-child(1)'.format(i))
            last_update_time = response.css('li.col-12:nth-child({}) > div:nth-child(1) > '
                                            'div:nth-child(3)'.format(i))
            try:
                value_last_update =last_update_time.css('relative-time::text').get()
                if value_last_update is not None:
                    yield {'title':title.css('a::text').get().strip(),
                           'path_to_repository':base_url + title.css('a::attr(href)').extract()[0],
                           'last_updated_on': value_last_update}
                else:
                    yield {'title': title.css('a::text').get().strip(),
                           'path_to_repository': base_url + title.css('a::attr(href)').extract()[0],
                           'last_updated_on': 'Never'}
            except Exception:
                print("Least than 30 repositories")
                break

        # next_page = response.css('.paging')
        # link_to_follow = next_page.css('a::attr(href)').extract()
        # for link in link_to_follow:
        #     yield response.follow(link, self.parse)

        next_page = response.css(".BtnGroup")
        if next_page.css("a::text").get() == "Next":
            new_page = next_page.css("a::attr(href)").extract()
            for __new_page in new_page:
                yield response.follow(__new_page, self.parse)
