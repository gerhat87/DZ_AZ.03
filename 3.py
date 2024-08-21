from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/w/index.php?search=Солнечная%20система&title=Служебная%3AПоиск&ns0=1')

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, 'div'):
    cl = element.get_attribute('class')
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)
print(hatnotes)
hatnote = random.choice(hatnotes)
link = hatnote.find_element(By.TAG_NAME, 'a').get_attribute('href')
browser.get(link)

