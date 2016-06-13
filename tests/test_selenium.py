import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestSelenium(unittest.TestCase):

    def test_phantomjs(self):
        driver = webdriver.PhantomJS() # add phantomjs to your PATH
        driver.set_window_size(1024, 768)
        driver.get('https://google.com/')
        sbtn = driver.find_element_by_css_selector('input[name="btnI"]')
        sbtn.click()


if __name__ == '__main__':
    unittest.main()
