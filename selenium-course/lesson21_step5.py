from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_css_selector('[id="answer"]').send_keys(y)
    checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]').click()
    radiobutton = browser.find_element_by_css_selector('[id="robotsRule"]').click()
    button = browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

