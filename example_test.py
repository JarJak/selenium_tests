import unittest

from functional import SeleniumTestCase


class NewVisitorTest(SeleniumTestCase):
    def test_google_can_find_me(I):
        I.amOnUrl('https://google.pl')
        I.fillField('input[type="text"]', 'SeleniumTestCase')
        I.submitForm()
        I.see('SeleniumTestCase')
        I.see('GitHub')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
