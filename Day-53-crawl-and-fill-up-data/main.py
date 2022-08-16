from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
response = requests.get(url, headers=headers)
# response.raise_for_status()
# data = response.json()
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
#Create a list of links for all the listings you scraped. e.g.
links = []
for link in soup.findAll('a', attrs={'data-test': 'property-card-link'}):
    links.append(link.get('href'))
# print(links)

all_links = []
for link in links:
    if "http" not in link:
        all_links.append(f"https://www.zillow.com{link}")
    else:
        all_links.append(link)
temp_link =[]
for link in all_links:
    if link not in temp_link:
        temp_link.append(link)
all_links = temp_link
print(all_links)
print(len(all_links))

#Create a list of prices for all the listings you scraped. e.g.
# prices = []
# for price in soup.findAll('span', attrs={'data-test': 'property-card-price'}):
#     print(price)
#     print(price.text)
#     prices.append(price)
# print(len(prices))
all_price_elements = [price.get_text().split("+")[0]
                      for price in soup.findAll('span', attrs={'data-test': 'property-card-price'})]
# print(all_price_elements)
all_price_elements = [price.split("/")[0] for price in all_price_elements]
print(all_price_elements)
print(len(all_price_elements))

#Create a list of addresses for all the listings you scraped. e.g.
all_addresses = [address.get_text().split(" | ")[-1] for address in soup.findAll('address', attrs={'data-test': 'property-card-addr'})]
print(all_addresses)
print(len(all_addresses))


chorme_driver_path = "C:\development\chromedriver.exe"
s = Service(chorme_driver_path)
questionare_link = "https://docs.google.com/forms/d/e/1FAIpQLSeAzigUOC86c9OzSZUsFHbGXp1r0I-AA2x2-I5OTqdbznmgNQ/viewform?usp=sf_link"
driver = webdriver.Chrome(service=s)

for fill in range(len(all_links)):
    driver.get(questionare_link)
    time.sleep(2)

    address = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[fill])
    price.send_keys(all_price_elements[fill])
    link.send_keys(all_links[fill])
    submit_button.click()