from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
PROMISED_DOWN = 150
PROMISED_UP = 10
chorme_driver_path = "C:\development\chromedriver.exe"
s = Service(chorme_driver_path)
account_name = "jack.helpenglish@gmail.com"
password = "01654000397a"
# PHONE ="0123456778"


class InternetSpeedBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        time.sleep(3)
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        time.sleep(3)
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        # self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/span[1]').click()
        # base_window = self.driver.window_handles[0]
        # tt_login_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(tt_login_window)
        print(self.driver.title)

        # Login and hit enter
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(account_name)
        email.send_keys(Keys.ENTER)
        password_tt = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')

        password_tt.send_keys(password)
        password_tt.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()
speed_test_web = InternetSpeedBot(s)
speed_test_web.get_internet_speed()
speed_test_web.tweet_at_provider()
