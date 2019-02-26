import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TwitSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.options =  self.driver.ChromeOptions()
        self.options.add_argument('headless')
        
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("localhost:5000")
        print(driver.title)
        #self.assertIn("Python", driver.title)
        elem = driver.find_element_by_id('searchForm')
        elem.send_keys("Twitter")
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
