import time
import math
from selenium import webdriver


def calc(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()

try:
    # Открывает страницу
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element_by_css_selector("button[type='submit']").click()

    browser.switch_to.window(browser.window_handles[1])

    xValue = int(browser.find_element_by_css_selector('#input_value').text)
    browser.find_element_by_css_selector('#answer').send_keys(str(calc(xValue)))

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
