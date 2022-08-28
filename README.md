This project provides three scrapers for scraping EnGadget,a technology gadgets website,and are written with BeautifulSoup4, Selenium and Scrapy modules. 

**Name:** Sevinj Guluyeva 
**Student No:** 444423 
**Student Email:** s.guluyeva@student.uw.edu.pl

## Usage
You can install requirements via pip.
`pip install -r requirements.txt`

Then, to run BeautifulSoup4 scraper you can type the command below:

`python engadget_soup_scraper.py`

To run Selenium scraper, you need a driver for Chrome. The driver must be compatible with installed Chrome version on your computer. A driver for Chrome version 104.x is given at selenium folder and it must be at the same directory as scraper:

`python engadget_selenium_scraper.py`

I uploaded two Selenium files. "Engadget_selenium_scraper_new.py" works in a new version Selenium.( June 2022 version)

To run Scrapy scraper, you need a scrapy binary. Spider itself can be run self-contained:

`scrapy runspider engadget_scrapy_scraper.py`

