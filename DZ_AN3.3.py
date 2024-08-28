import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(5)  # Подождем, пока страница полностью загрузится

# Найдем все карточки продуктов
divans = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

parsed_data = []

for divan in divans:
    try:
        # Извлекаем название продукта
        name = divan.find_element(By.CSS_SELECTOR, 'div.lsooF span').text.strip()
        # Извлекаем цену продукта
        price = divan.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text.strip()
        # Извлекаем ссылку на продукт
        url = divan.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    # Добавляем данные в список
    parsed_data.append([name, price, url])

# Закрываем браузер
driver.quit()

# Сохраняем данные в CSV файл
with open("divan_products.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'URL'])
    writer.writerows(parsed_data)