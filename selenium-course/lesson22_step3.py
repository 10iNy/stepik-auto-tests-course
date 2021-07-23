from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x, y):
  return str(x+y)
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector('#num1').text
    num2 = browser.find_element_by_css_selector('#num2').text
    answer = str(int(num1) + int(num2))
    #answer = calc(int(num1), int(num2))
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(answer)
    button = browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

