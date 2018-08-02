# -*from scrapy import spider
from time import sleep
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException

class RestaurantSpider(Spider):
    name = 'Restaurant'
    allowed_domains = ['dineout.co.in']
    #start_urls = ['http://dineout.co.in/bangalore-restaurants?search_str=']

    def start_requests(self):
        self.logger.info('<-----Starting the driver----->')
        # Creating new Instance of Chrome
        self.driver = webdriver.Chrome('/Users/macbookpro/Downloads/chromedriver')

        # Going to desired website
        self.driver.get('https://www.dineout.co.in/bangalore-restaurants?search_str=')
        sel = Selector(text=self.driver.page_source)

        self.logger.info('<-----Getting Urls on first page----->')
        # Getting the restaurant's url on th first page and parsing it to get
        # the details like Name, Location, Address, Rating, Reviews, Map_link
        restaurantUrls = sel.xpath('//h4/a/@href').extract()
        for restaurantUrl in restaurantUrls:
            url = 'https://www.dineout.co.in' + restaurantUrl
            self.parse_restaurant(url)

        for i in range(1, 250):
            try:
                # Going to the next pages and Getting the hotel's list url on
                # those pages and parsing it as we did for the first page
                next_page = self.driver.find_element_by_xpath('//a[text()="Next "]')
                sleep(7)
                self.logger.info('<-----Sleeping for 7 seconds----->')
                self.logger.info('<-----Clicking the next page----->')
                next_page.click()

                sel = Selector(text=self.driver.page_source)
                self.logger.info('<-----Getting Urls on next page----->')
                restaurantUrls = sel.xpath('//h4/a/@href').extract()
                for restaurantUrl in restaurantUrls:
                    url = 'https://www.dineout.co.in' + restaurantUrl
                    yield Request(url, callback=self.parse_restaurant)

            except NoSuchElementException as e:
                # Exiting the driver when a element is not found
                self.logger.info('<-----Stoping the driver----->')
                self.driver.quit()
                break
    #In this definition we define the details that needs to be collected
    def parse_restaurant(self, response):

        name = response.xpath('//*[@class="restnt-name"]/text()').extract_first()
        location = response.xpath('//*[@class="restnt-loc"]/a/text()').extract()
        rating = response.xpath('//*[@class="rating rating-5"]/text()').extract_first()
        address = response.xpath('//*[@class="address-info"]/text()').extract_first()        
        reviews = response.xpath('//*[@class="right"]/p/span[@class="more"]/text()').extract_first()
        map_link = response.xpath('//*[@class="rightDiv address-wrap col-sm-9"]/div/a/@href').extract_first()

        yield{
        'Name': name,
        'Location': location,
        'Rating': rating,
        'URL': response,
        'Address': address,
        'Reviews': reviews,
        'Map_link': map_link
        }
        pass