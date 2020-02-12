import time
import os
from selenium import webdriver

browser = webdriver.Chrome()
current_directory = os.path.abspath(os.path.dirname(__file__))

try:
    # Открывает страницу
    browser.get('http://suninjuly.github.io/file_input.html')

    browser.find_element_by_css_selector('form [name="firstname"]').send_keys('Sergey')
    browser.find_element_by_css_selector('form [name="lastname"]').send_keys('Shv')
    browser.find_element_by_css_selector('form [name="email"]').send_keys('some-mail@mail.com')
    browser.find_element_by_css_selector('input#file').send_keys(os.path.join(current_directory, 'test-file.txt'))

    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(5)
    browser.quit()
