import scrapy
from bs4 import BeautifulSoup

class travelBlagCrawler(scrapy.Spider):
    name = 'worldtravelfamily'
    start_urls = ['https://worldtravelfamily.com/vietnam-travel-blog/']

    def parse(self, response):
        for tag in response.css('#post-35315'):
            i = 2
            while i <= 140:
                sel = 'p:nth-child(' + str(i) + ')'
                sel1 = 'h3:nth-child(' + str(i) + ')'
                sel2 = 'h4:nth-child(' + str(i) + ')'
                tmp = tag.css(sel).get()
                tmp1 = tag.css(sel1).get()
                tmp2 = tag.css(sel2).get()
                i += 1
                if tmp is not None:
                    yield {'info': tmp}
                elif tmp1 is not None:
                    yield {'section': tmp1}
                elif tmp2 is not None:
                    yield {'subsection': tmp2}
                else:
                    continue

#post-35315 > p:nth-child(2)
#post-35315 > p:nth-child(3)
#post-35315 > h3:nth-child(6)

#post-35315 > p:nth-child(140)