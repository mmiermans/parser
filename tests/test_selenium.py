import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSelenium(unittest.TestCase):
    
    def test_selenium(self):
        driver = webdriver.Firefox()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()



if __name__ == '__main__':
    unittest.main()
