from selenium import webdriver

# Указываем путь к драйверу (например, для Chrome)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

driver.get('https://www.google.com')
print(driver.title)

driver.quit()
