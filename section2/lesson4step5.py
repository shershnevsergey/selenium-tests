import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

try:
    # Открывает страницу
    browser.get('http://suninjuly.github.io/wait1.html')

    browser.find_element_by_id('verify').click()
    message = browser.find_element_by_id('verify_message')

    assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()
