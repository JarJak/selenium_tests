from selenium import webdriver
import unittest
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


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

    def submitForm(self, css: str):
        field = self._jq(css)
        field.send_keys(Keys.ENTER)

    def seeInField(self, css: str, content: str):
        field = self._jq(css)
        self.assertTrue(content, field.get_attribute('value'))

    def dontSeeInField(self, css: str, content: str):
        field = self._jq(css)
        self.assertFalse(content, field.get_attribute('value'))

    def refreshPage(self):
        self.browser.refresh()


