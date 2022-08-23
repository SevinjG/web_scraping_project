from itertools import product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common import exceptions  
import sys
import time



headers = {
    'accept': 'text/html',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}



if __name__ == "__main__":
    main_url = "https://www.engadget.com"

    # Selenium options for running Chrome headless 
    options = Options()
    options.headless = True
    options.add_argument('log-level=3')
    # Windows
    driver = webdriver.Chrome('.\\chromedriver.exe',options=options)
    
    categories = ["laptops","phones","gaming-consoles-home","headphones","televisions","tablets","wearables","cameras","routers","external-drives"]
    start_time = time.perf_counter()

    category_dict = {}
    for category in categories:
        driver.get(main_url + "/products/"+category)
        hrefs = driver.find_elements_by_xpath("//a[@class='StretchedBox']")
        product_dict = {}
        for href in hrefs:
            try:
                #href.get_attribute("href") -> returns complete url
                product_name = href.get_attribute("href").split("/")[-2]
                driver.get(href.get_attribute("href"))
                score = ""
                productScores = driver.find_elements_by_xpath("//h3")
                if productScores == []:
                    continue

                for i in range(1,6,2):
                    score += productScores[i].text + ","
                product_dict[product_name] = score
            except exceptions.StaleElementReferenceException:
                continue


        category_dict[category] = product_dict.copy()
        product_dict.clear()

    end_time = time.perf_counter()
    # score sum for each category to further analysis for score of each category
    category_engadget_score = []
    for category,products in category_dict.items():
        print(f"=========={category}================")
        tmp_score = 0
        for product,score in products.items():
            score_list = score.split(",")[:-1] # remove last empty element from the list
            engadget_score = int(score_list[0])
            tmp_score += engadget_score
            print(f"Score for product {product}:")
            print(f"\t> Engadget Score:{score_list[0]}\n\t> Critics Score:{score_list[1]}\n\t> Users Score:{score_list[2]}\n")
        category_engadget_score.append(tmp_score)
        print(f"Category {category} Engadget Score: {tmp_score}")
        print("================================")

    print("Further analysis can be done by user.")
    print("Performance for Selenium scraper as seconds is:",end_time - start_time)
    sys.exit(0)
