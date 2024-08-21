from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Создаем экземпляр браузера
driver = webdriver.Chrome()  # Замените на ваш браузер

def search_wikipedia(query):
    # Переходим на страницу Википедии
    driver.get("https://wikipedia.org")
    # Вводим запрос в поле поиска
    search_input = driver.find_element(By.NAME, "search")
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)
    # Ждем, пока страница загрузится
    time.sleep(2)

def list_paragraphs():
    # Получаем список параграфов на странице
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    for paragraph in paragraphs:
        print(paragraph.text)

def get_related_links():
    # Получаем список связанных страниц
    links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/wiki/']")
    return links

def main():
    # Спрашиваем у пользователя первоначальный запрос
    query = input("Введите запрос: ")
    search_wikipedia(query)

    while True:
        print("Выберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == "1":
            list_paragraphs()
        elif choice == "2":
            links = get_related_links()
            print("Выберите связанную страницу:")
            for i, link in enumerate(links):
                print(f"{i+1}. {link.text}")
            link_choice = input("Введите номер страницы: ")
            link = links[int(link_choice) - 1]
            link.click()
            time.sleep(2)
            print("Вы перешли на страницу:", driver.title)
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    # Закрываем браузер
    driver.quit()

if __name__ == "__main__":
    main()