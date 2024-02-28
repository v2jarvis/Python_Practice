#simple practice of selenium
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com")
#time.sleep(10)
input("Press Enter to close the browser...")