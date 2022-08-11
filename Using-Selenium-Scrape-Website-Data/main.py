from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chorme_driver_path = "C:\development\chromedriver.exe"
s = Service(chorme_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")
event_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# event_time = driver.find_elements(By.CSS_SELECTOR, '.medium-widget event-widget last time')
event_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}
for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_name[n].text,
    }
print(events)
driver.quit()
