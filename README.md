SeleniumTestCase
================

Class created in python to ease functional testing with selenium. It's basically a wrapper for Selenium Webdriver with methods inspired by Facebook Webdriver (from Codeception) - but it's much faster and less buggable than Codeception itself.

It will be expanded to cover all methods from [Codeception Webdriver](http://codeception.com/docs/modules/WebDriver).
Do you need any new method? Found a bug? Please create an issue or send PR :)

Usage:
------

You need only one file: functional.py. It has a class SeleniumTestCase which you should extend.
Default setup uses Chrome browser. Need Firefox or any custom options? Just override setUp() method.


Example:
--------

Example test class (from example_test.py):

```python
from functional import SeleniumTestCase
import unittest


class NewVisitorTest(SeleniumTestCase):

    def test_google_can_find_me(I):
        I.amOnUrl('https://google.pl')
        I.fillField('input[type="text"]', 'SeleniumTestCase')
        I.submitForm()
        I.see('SeleniumTestCase')
        I.see('GitHub')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
```

Now run it:

```
python example_test.py
```

If no Error will be thrown - test pass!

Todo
----

 - concurrency tests
