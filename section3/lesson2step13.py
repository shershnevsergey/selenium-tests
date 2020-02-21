# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import unittest

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome()


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def fill_form(self, url):
        # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        browser.get(url)

        browser.find_element_by_css_selector('.first_block div.first_class input.first').send_keys('Мой ответ')
        browser.find_element_by_css_selector('.first_block div.second_class input.second').send_keys('Мой ответ')
        browser.find_element_by_css_selector('.first_block div.third_class input.third').send_keys('Мой ответ')

        browser.find_element_by_css_selector('button.btn').click()

        return browser.find_element_by_tag_name('h1').text

    def testRegistration1Page(self):
        link = 'http://suninjuly.github.io/registration1.html'
        expected_text = 'Congratulations! You have successfully registered!'

        self.assertEqual(self.fill_form(link), expected_text, "success text is not equals to {}".format(expected_text))

    def testRegistration2Page(self):
        link = 'http://suninjuly.github.io/registration2.html'
        expected_text = 'Congratulations! You have successfully registered!'

        self.assertEqual(self.fill_form(link), expected_text, "success text is not equals to {}".format(expected_text))

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
