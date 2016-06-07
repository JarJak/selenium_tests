import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# @docs http://selenium-python.readthedocs.org/api.html#module-selenium.webdriver.chrome.webdriver
# inspired by http://codeception.com/docs/modules/WebDriver
class SeleniumTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def _jq(self, css):
        return self.browser.find_element_by_css_selector(css)

    def _jqs(self, css: str):
        return self.browser.find_elements_by_css_selector(css)

    def see(self, text: str, css: str = 'body'):
        self.assertIn(text, self._jq(css).text)

    def dontSee(self, text: str, css: str = 'body'):
        self.assertNotIn(text, self._jq(css).text)

    def seeElement(self, css: str):
        self.assertTrue(self._jq(css))

    def dontSeeElement(self, css: str):
        try:
            self._jq(css)
            self.assertFalse(True)
        except NoSuchElementException:
            self.assertFalse(False)

    def wait(self, seconds: int):
        time.sleep(seconds)

    def amOnUrl(self, url: str):
        self.browser.get(url)

    def click(self, css: str):
        self._jq(css).click()

    def seeCookie(self, name: str):
        self.assertTrue(self.browser.get_cookie(name))

    def dontSeeCookie(self, name: str):
        self.assertFalse(self.browser.get_cookie(name))

    def finish(self):
        self.fail('THE END')

    def fillField(self, css: str, content: str):
        field = self._jq(css)
        field.send_keys(content)

    def selectOption(self, css: str, text: str):
        field = self._jq(css)
        for option in field.find_elements_by_tag_name('option'):
            if option.text == text:
                option.click()
                return
        raise NoSuchElementException('Element '+css+' has no option '+text)

    def submitForm(self, css: str = 'form'):
        field = self._jq(css)
        field.submit()

    def seeInField(self, css: str, content: str):
        field = self._jq(css)
        self.assertEquals(content, field.get_attribute('value'))

    def dontSeeInField(self, css: str, content: str):
        field = self._jq(css)
        self.assertNotEquals(content, field.get_attribute('value'))

    def refreshPage(self):
        self.browser.refresh()
