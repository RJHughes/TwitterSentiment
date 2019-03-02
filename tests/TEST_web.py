import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TwitSearch(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("localhost:5000/search")
        #print(driver.title)
        #self.assertIn("Python", driver.title)
        elem = driver.find_element_by_id('searchForm')
        elem.send_keys("Twitter")
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
