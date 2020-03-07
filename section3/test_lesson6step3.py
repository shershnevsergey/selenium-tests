import pytest
import time
import math


@pytest.mark.parametrize('lesson_id', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_guest_should_see_login_link(browser, lesson_id):
    browser.get("https://stepik.org/lesson/{}/step/1".format(lesson_id))
    browser.find_element_by_css_selector('textarea').send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector('.submit-submission').click()
    result_message = browser.find_element_by_css_selector('.smart-hints__hint').text

    assert result_message == 'Correct!', 'Real text is: {}'.format(result_message)


# pytest -s -v test_lesson6step3.py
