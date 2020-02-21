# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration2.html'

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome()

try:
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get(link)

    browser.find_element_by_css_selector('.first_block div.first_class input.first').send_keys('Мой ответ')
    browser.find_element_by_css_selector('.first_block div.second_class input.second').send_keys('Мой ответ')
    browser.find_element_by_css_selector('.first_block div.third_class input.third').send_keys('Мой ответ')

    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(1)

    success_text = browser.find_element_by_tag_name('h1').text

    assert 'Congratulations! You have successfully registered!' == success_text
finally:
    time.sleep(10)
    browser.quit()
