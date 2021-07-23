from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    #browser.implicitly_wait(12)
    browser.get(link)
    required = str(100)

    sotka = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id("book").click()
    value = browser.find_element_by_id("input_value").text
    answer = calc(value)
    browser.find_element_by_css_selector(".form-control").send_keys(answer)
    browser.find_element_by_id("solve").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
