import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    # Открывает страницу
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    browser.find_element_by_css_selector('#book').click()

    x_value = int(browser.find_element_by_css_selector('#input_value').text)
    browser.find_element_by_css_selector('#answer').send_keys(str(calc(x_value)))

    browser.find_element_by_css_selector("#solve").click()

finally:
    time.sleep(5)
    browser.quit()
