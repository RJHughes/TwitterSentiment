import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TwitSearch(unittest.TestCase):
    def setUp(self):

        self.options = Options()
        #self.options.add_argument('headless')
        self.options.add_argument("--no-sandbox");
        self.options.add_argument("--disable-dev-shm-usage");
        self.driver = webdriver.Chrome(chrome_options=self.options)

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
