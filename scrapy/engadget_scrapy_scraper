import scrapy



headers = {
    'accept': 'text/html',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}


class EngadgetSpider(scrapy.Spider):
    name = "engadgetSpider"
    main_url = "https://www.engadget.com"

    
    categories = ["laptops","phones","gaming-consoles-home","headphones","televisions","tablets","wearables","cameras","routers","external-drives"]
    start_urls = [main_url+"/products/"+categories.pop(0)]
    result_dict = {}
    # will be used for each products of a category
    product_dict = {}
    productUrls = []
    url = ""
    productUrl = ""

    def yield_category(self):
        if self.productUrls:
            self.productUrl = self.productUrls.pop(0)
            print("\t > Scraping",self.productUrl)
            return scrapy.Request(self.main_url+self.productUrl,callback=self.parse_product)
        else:
            self.result_dict[self.url] = self.product_dict.copy()
            self.product_dict.clear()

        if self.categories:
            self.url = self.categories.pop(0)
            print("Scraping category ",self.url)
            return scrapy.Request(self.main_url+"/products/"+self.url,callback=self.parse)
        else:
            self.printResult()
            print("All categories are done! Check Scrapy stats from screen for performance metrics!")

    def parse(self,response):
        # Products are classified as "StretchedBox"
        hrefs = response.xpath("//a[@class='StretchedBox']")
        # Product urls to pass to scraper
        self.productUrls = hrefs.css("a::attr(href)").extract()
        
        yield self.yield_category()

    def parse_product(self,response):

        # Product scores are kept in h3 tags
        productScores = response.xpath("//h3/text()").extract()
        
        try:
            self.product_dict[response.request.url.split("/")[-2]] = productScores[1] + "," + productScores[3] + "," + productScores[5]
            yield self.yield_category()
        except:
            yield self.yield_category()

    def printResult(self):
        # In Python 3, dictionaries are ordered dict by default. So, any score index we append to category_engadget_score list will be the same index for categories list
        for category,products in self.result_dict.items():
            print(f"=========={category}================")
            tmp_score = 0
            for product,score in products.items():
                score_list = score.split(",")
                engadget_score = int(score_list[0])
                tmp_score += engadget_score
                print(f"Score for product {product}:")
                print(f"\t> Engadget Score:{score_list[0]}\n\t> Critics Score:{score_list[1]}\n\t> Users Score:{score_list[2]}\n")
            print(f"Category {category} Engadget Score: {tmp_score}")
            print("================================")
