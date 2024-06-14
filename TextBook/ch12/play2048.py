from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://rugugu.jp/2048/')
html = browser.find_element(By.TAG_NAME, 'html')

print('停止するにはCTRL-Cを押してください。')

try:
    while True:
        html.send_keys(Keys.UP)
        time.sleep(0.1)
        html.send_keys(Keys.RIGHT)
        time.sleep(0.1)
        html.send_keys(Keys.DOWN)
        time.sleep(0.1)
        html.send_keys(Keys.LEFT)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('終了')

