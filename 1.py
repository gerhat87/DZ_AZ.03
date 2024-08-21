from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/Заглавная_страница')

assert 'Википедия' in browser.title
time.sleep(4)
searh_box = browser.find_element(By.ID, 'searchInput')
searh_box.send_keys('Солнечная система')
searh_box.send_keys(Keys.RETURN)

time.sleep(4)
a= browser.find_element(By.LINK_TEXT, 'Солнечная система')
a.click()