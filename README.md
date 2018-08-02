Dineout Restaurant Business Details Scraper
-----------------------------------------------------
Dineout.com Web Scraper written in Python. Scrapy framework and Selenium web driver is used alongside to extract Restaurant details available based on a particular city

-----------------------------------------------------
Getting Started
-----------------------------------------------------
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

-----------------------------------------------------
Fields to Extract
-----------------------------------------------------
This Dineout Restaurant scraper can extract the fields below:

Restaurant Name
Locality
Full Address
Rating
Reviews on the Detail page
MapLink(TO locate the Restaurants in the Google Maps)

-----------------------------------------------------
Prerequisites
-----------------------------------------------------
For this web scraping to run will be using Python 2.7, we will need some packages to automate the NEXT button click as the url is going to remain static. Below are the package that we will use to leverage our solution:

Selenium Webdriver
Chrome Driver

-----------------------------------------------------
Installation
-----------------------------------------------------
PIP to install the following packages in Python (https://pip.pypa.io/en/stable/installing/)

1]Python Requests, to make requests and download the HTML content of the pages (http://docs.python-requests.org/en/master/user/install/)
2] $ pip install scrapy --> Scrapy framework, to crawl the website(https://scrapy.org/)
3] $ pip install selenium --> Selenium, to automate the browser interaction(http://selenium-python.readthedocs.io/installation.html)
4]ChromeDriver(can be downloaded from here: http://chromedriver.chromium.org/downloads)

-----------------------------------------------------
Running the scraper
-----------------------------------------------------
We would execute the code with the spider name followed by the output file name and format in which the output is to be downloaded. Here is how to run the spider

scarpy crawl Restaurant -o Restaurant.csv

-----------------------------------------------------
Sample Output
-----------------------------------------------------
This will create a csv file:

Restaurant.csv