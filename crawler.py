from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 設定瀏覽器選項
options = Options()
# 建立 driver
s = Service()
chrome = webdriver.Chrome(service=s, options=options)
# 存取 Website
url = "https://www.google.com.tw/"
chrome.get(url)
# 等待 5 秒鐘以載入頁面
time.sleep(10)
search_input = chrome.find_element(By.NAME, "q")
search_input.send_keys("Python")

search_input.send_keys(Keys.RETURN)
time.sleep(10)

# 關閉瀏覽器視窗
chrome.close()
