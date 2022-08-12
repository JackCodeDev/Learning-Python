from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


from selenium.webdriver.common.keys import Keys
chorme_driver_path = "C:\development\chromedriver.exe"
s = Service(chorme_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cake_click = driver.find_element(By.ID, "cookie")

# buy_cursor = driver.find_element(By.ID, "buyCursor")
# buy_grandma = driver.find_element(By.ID, "buyGrandma")
# cookie_per_s = driver.find_element(By.ID, "cps").text

#Get upgrade item ids. Take all id items to store
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# print(items[1].text)

item_ids = [item.get_attribute("id") for item in items]
print(item_ids)
timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cake_click.click()
    # Every 5 seconds:
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_price = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            # print(element_text)
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_price.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_price)):
            cookie_upgrades[item_price[n]] = item_ids[n]

        #Check cake_score/cookie_count
        cake_score = driver.find_element(By.ID, "money").text
        if "," in cake_score:
            money_element = cake_score.replace(",", "")
        cookie_count = int(cake_score)

        #Find upgrades that we can currently afford to store in other dict
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
                # print(affordable_upgrade)

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()
        #Add another 5 seconds until the next check
        timeout = time.time() + 5
        # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, "cps").text
            print(cookie_per_s)
            break






    # driver.get("http://secure-retreat-92358.herokuapp.com/")

# english = driver.find_element(By.PARTIAL_LINK_TEXT, 'English')
# # english.click()
# #
# # search = driver.find_element(By.NAME, "search")
# # search.send_keys("Python")
# # search.send_keys(Keys.ENTER)
#
# first_name = driver.find_element(By.NAME, "fName")
# first_name.send_keys("Jack")
#
# last_name = driver.find_element(By.NAME, "lName")
# last_name.send_keys("Nguyen")
#
# email_address = driver.find_element(By.NAME, "email")
# email_address.send_keys("jack.helpenglish@gmail.com")
#
# sign_up = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")
# sign_up.click()

# print(article_count.text.split()[0])
# driver.quit()

