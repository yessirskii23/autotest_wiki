import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_navigation():
    # Открываем браузер и главную страницу Википедии
    print("Открываем главную страницу Википедии...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://ru.wikipedia.org/")

    try:
        # Ожидаем, что страница загрузится
        time.sleep(2)

        # Переходим на случайную статью
        print("Перехожу на случайную статью...")
        random_article_link = driver.find_element(By.LINK_TEXT, "Случайная статья")
        random_article_link.click()

        # Ожидаем, пока страница случайной статьи загрузится
        time.sleep(3)

        # Проверяем, что URL изменился, и печатаем текущий URL
        current_url = driver.current_url
        print(f"Текущий URL: {current_url}")
        print("Навигация успешна, мы на случайной статье.")

        # Прокручиваем страницу вниз
        print("Скроллим страницу...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ожидаем, чтобы дать время на прокрутку
        time.sleep(3)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("Закрываем браузер...")
        driver.quit()


if __name__ == "__main__":
    test_navigation()
