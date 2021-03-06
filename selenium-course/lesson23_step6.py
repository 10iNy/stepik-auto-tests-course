from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    value = browser.find_element_by_css_selector("#input_value").text
    answer = calc(value)
    browser.find_element_by_css_selector(".form-control").send_keys(answer)
    browser.find_element_by_tag_name("button").click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
