import scrapy
from bs4 import BeautifulSoup

# since trip advisor has bigger db than a blog so only crawl on selected cities: Hanoi, HCM, Danang, Hue,
# Hoian, Halong, Sapa

# declare as a pre-defined list as it has specific code attached to city
# for more cities, declare and added to this list
# the structure of each website is not consistent so there are not 

LIST_OF_INTERESTED_CITIES = {'Ha Noi': 'g293924-Hanoi', 'HO Chi Minh City': 'g293925-Ho_Chi_Minh_City',
                             'Da Nang': 'g298085-Da_Nang', 'Hue': 'g293926-Hue_Thua_Thien_Hue_Province',
                             'Hoi An': 'g298082-Hoi_An_Quang_Nam_Province',
                             'Ha Long': 'g293923-Halong_Bay_Quang_Ninh_Province',
                             'Sapa': 'g311304-Sapa_Lao_Cai_Province'}
BASE_GEO_CODE = 'g293921-Vietnam'
BASE_URL = 'https://www.tripadvisor.com/Tourism-g293921-Vietnam-Vacations.html'


class tripCrawler(scrapy.Spider):
    name = 'tripadvisor'
    start_urls = list(BASE_URL.replace(BASE_GEO_CODE, item) for key, item in LIST_OF_INTERESTED_CITIES.items())
    # for search in BFS instead of the default behaviors which is DFS order plus async thus can make the return list on
    # an undesirable order. however, as we force crawler to has 1 concurrent_request and 1 concurrent_request_per_id,
    # the crawler will be slow
    custom_settings = {'CONCURRENT_REQUESTS': 1, 'CONCURRENT_REQUESTS_PER_IP': 1, 'DEPTH_PRIORITY': 2,
                       'SCHEDULER_DISK_QUEUE': 'scrapy.squeues.PickleFifoDiskQueue',
                       'SCHEDULER_MEMORY_QUEUE': 'scrapy.squeues.FifoMemoryQueue'}


    # parse the main site
    # get hotel, thing to do and restaurant only
    def parse(self, response):
        url = response.request.url
        loc = list(LIST_OF_INTERESTED_CITIES.keys())
        # city will not be declare before loop as there are no need for the case of outside the list.
        for key, item in LIST_OF_INTERESTED_CITIES.items():
            if item in url:
                city = key
                break
        base_url = 'https://www.tripadvisor.com'
        for tag in response.css('._1ZteHrEy'):
            if LIST_OF_INTERESTED_CITIES[loc[0]] in url or LIST_OF_INTERESTED_CITIES[loc[1]] in url:
                for i in [2, 4, 5]:
                    sel = 'div:nth-child(' + str(i) + ') > a'
                    relative_link = tag.css(sel).xpath('@href').get()
                    try:
                        title = tag.css(sel).xpath('@title').extract()[0]
                    except IndexError:
                        title = tag.css(sel).xpath('@title').extract()
                    child_page = base_url + relative_link
                    yield scrapy.Request(response.urljoin(child_page),
                                         callback=self.parse_child_page,
                                         meta={'title': title, 'city': city, 'type': title, 'grouplink': child_page})
            else:
                for i in [1, 3, 4]:
                    sel = 'div:nth-child(' + str(i) + ') > a'
                    relative_link = tag.css(sel).xpath('@href').get()
                    try:
                        title = tag.css(sel).xpath('@title').extract()[0]
                    except IndexError:
                        title = tag.css(sel).xpath('@title').extract()
                    try:
                        child_page = base_url + relative_link
                    except TypeError:
                        # having 1 more node
                        sel = 'div:nth-child(' + str(i + 1) + ') > a'
                        relative_link = tag.css(sel).xpath('@href').get()
                        try:
                            title = tag.css(sel).xpath('@title').extract()[0]
                        except IndexError:
                            title = tag.css(sel).xpath('@title').extract()
                        child_page = base_url + relative_link
                    yield scrapy.Request(response.urljoin(child_page),
                                         callback=self.parse_child_page,
                                         meta={'title': title, 'city': city, 'type': title, 'grouplink': child_page})

    # parse one child page
    # after inspect, check content of each child page this func will become the selector to each type of child page
    # (kind of like switch case)
    def parse_child_page(self, response):
        title = response.meta.get('title')
        city = response.meta.get('city')
        type = response.meta.get('type')
        link = response.meta.get('grouplink')
        # switch(title)
        # case == Hotels
        names = []
        if title == 'Hotels':
            hotel = response.css('#taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0')
            sel_name = '//*[@data-clicksource="HotelName"]/text()'
            sel_rating = '//*[contains(@class, "ui_bubble_rating")]'
            places = hotel.xpath(sel_name).extract()
            rating = hotel.xpath(sel_rating).css('::attr(alt)').extract()
            pair_place_rating = list(zip(places, rating))
            for pair in pair_place_rating:
                yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0],
                       'Rating': pair[1].split(' bubbles')[0]}
        # case == Things to Do
        elif title == 'Things to Do':
            interested_places = response.css('#FILTERED_LIST')
            sel_name = '//*[contains(@class, "_20eVZLwe")]//a[contains(@class, "_3W3bcspL")]/h3/text()'
            sel_rating = '//*[contains(@class, "ui_poi_review_rating  ")]/span'
            places = interested_places.xpath(sel_name).extract()
            rating = interested_places.xpath(sel_rating).css('::attr(class)').extract()
            pair_place_rating = list(zip(places, rating))
            for pair in pair_place_rating:
                if '50' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '5 of 5'}
                elif '45' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '4.5 of 5'}
                elif '40' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '4 of 5'}
                elif '35' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '3.5 of 5'}
                elif '30' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '3 of 5'}
                elif '25' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '2.5 of 5'}
                elif '20' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '2 of 5'}
                elif '15' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '1.5 of 5'}
                elif '10' in pair[1]:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '1 of 5'}
                else:
                    yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': '0 of 5'}
        # case == Restaurants
        elif title == 'Restaurants':
            restaurant = response.css('#component_2')
            sel_name = '//div[contains(@class, "_1kXteagE")]//div[contains(@data-test, "SL_list_item")]//' \
                       '*[contains(@class, "_15_ydu6b")]//text()'
            sel_rating = '//*[contains(@class, "_1p0FLy4t")]'
            places = restaurant.xpath(sel_name).extract()
            # 1 place == 2 rating
            rating = restaurant.xpath(sel_rating).css('a::attr(class)').extract()
            pair_place_rating = []
            for i in range(len(places)):
                if '_2vB__cbb' in rating[i]:
                    pair_place_rating.append((places[i], '5 of 5'))
                elif '_1RZqMyqR' in rating[i]:
                    pair_place_rating.append((places[i], '4.5 of 5'))
                else:
                    pair_place_rating.append((places[i], '4 of 5'))
            # rating[2*i].strip('.') + '. ' + rating[2*i + 1].strip('.') + '.'
            for pair in pair_place_rating:
                yield {'City': city, 'Type': type, 'groupLink': link, 'Places': pair[0], 'Rating': pair[1]}
        # default (e.g. when pass a random obj in the field)
        else:
            return {'City': city, 'Type': type, 'groupLink': link, 'Places': 'Not Found', 'Rating': 'Not Found'}
