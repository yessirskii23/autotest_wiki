from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка драйвера
driver = webdriver.Chrome()
driver.maximize_window()

try:
    print("Открываем главную страницу Википедии...")
    driver.get("https://ru.wikipedia.org/")

    # Ожидаем появления кнопки 'Войти' на странице
    print("Ожидаем появления кнопки 'Войти'...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Войти']")))

    # Нажимаем на кнопку 'Войти'
    login_button.click()

    # Ожидаем появления полей для ввода логина и пароля
    print("Ожидаем появления формы входа...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wpName1")))

    # Вводим логин
    username_field = driver.find_element(By.ID, "wpName1")
    username_field.send_keys("TestSelenium11")

    # Вводим пароль
    password_field = driver.find_element(By.ID, "wpPassword1")
    password_field.send_keys("TestSelenium1122")

    # Нажимаем кнопку "Войти"
    login_button = driver.find_element(By.ID, "wpLoginAttempt")
    login_button.click()

    # Ожидаем, пока страница не загрузится после входа
    WebDriverWait(driver, 10).until(EC.title_contains("Википедия"))

    print("Успешно вошли в систему!")

finally:
    time.sleep(5)  # Ждем несколько секунд, чтобы увидеть результат
    driver.quit()  # Закрываем браузер

