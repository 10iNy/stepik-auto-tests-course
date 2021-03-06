from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_css_selector("#input_value").text
    y= calc(x_element)
    answer = browser.find_element_by_css_selector(".form-control").send_keys(y)
    button = browser.find_element_by_css_selector('[type="submit"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
