from selenium import webdriver
import time
import os
    
try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    required_elements = browser.find_elements_by_css_selector(".form-control")
    for element in required_elements:
        element.send_keys("Test")

    file_path = os.path.join(current_dir, 'file.txt')
    upload = browser.find_element_by_css_selector('#file')
    upload.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
