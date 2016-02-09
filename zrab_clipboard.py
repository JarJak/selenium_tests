from functional import SeleniumTestCase
import unittest


# @docs http://selenium-python.readthedocs.org/api.html#module-selenium.webdriver.chrome.webdriver
class NewVisitorTest(SeleniumTestCase):

    def disable_popup(self):
        self.browser.add_cookie({'name': 'visitedShop', 'value': '1'})
        self.browser.add_cookie({'name': 'visitedHome', 'value': '1'})

    def test_clipboard(self):
        I = self
        I.amOnUrl('https://zrabatowani.pl')
        I.dontSeeCookie('clipboard')
        self.disable_popup()
        I.amOnUrl('https://zrabatowani.pl/shop/matras')
        I.click('.campaign-box:first-child .add-to-clipboard')
        I.seeElement('.campaign-box:first-child .remove-from-clipboard')
        I.amOnUrl('https://zrabatowani.pl/panel/clipboard')
        I.seeCookie('clipboard')
        I.see('Matras', '.campaign-box')
        I.seeElement('.campaign-box:first-child .remove-from-clipboard')
        I.click('.campaign-box:first-child .remove-from-clipboard')
        I.wait(1)
        I.refreshPage()
        I.dontSeeElement('.campaign-box')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
