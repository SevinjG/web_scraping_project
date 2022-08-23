import requests
import bs4
import sys
import time



headers = {
    'accept': 'text/html',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}


if __name__ == "__main__":
    main_url = "https://www.engadget.com"

    
    categories = ["laptops","phones","gaming-consoles-home","headphones","televisions","tablets","wearables","cameras","routers","external-drives"]

    start_time = time.perf_counter()
    # url dictionary variable to hold urls for products in a category
    category_dict = {}
    for category in categories:
        # we need to add '/products/' to complete url here
        response = requests.get(main_url+"/products/"+category,headers=headers)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        # We get products for a category
        hrefs = soup.find_all("a",class_="StretchedBox")
        #print(len(hrefs))
        product_dict = {}
        # loop to get products' info and put them to product dictionary
        for href in hrefs:
            product_name = href["href"].split("/")[-2]
            response = requests.get(main_url+href["href"],headers=headers)
            soup = bs4.BeautifulSoup(response.content, 'html.parser')
            # score will be written as <engadget score>,<critics score>,<user score>
            score = ""
            productScores = soup.find_all("h3")
            # some pages cannot be found and redirect to different page. So we skip them here
            if productScores == []:
                continue
            # productScores[1] == <engadget_score , productScores[3] == <critics score>, productScores[5] == <user score>
            for i in range(1,6,2):
                score += productScores[i].text + ","
            product_dict[product_name] = score



        category_dict[category] = product_dict.copy()
        product_dict.clear()
        
    
    end_time = time.perf_counter()
    # score sum for each category to further analysis for score of each category
    category_engadget_score = []
    # In Python 3, dictionaries are ordered dict by default. So, any score index we append to category_engadget_score list will be the same index for categories list
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
    print("Performance for bs4 scraper as seconds is:",end_time - start_time)
    sys.exit(0)
