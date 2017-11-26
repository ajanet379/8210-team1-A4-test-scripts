import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_edit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_edit_client(self):
        user = "test"
        pwd = "test1234"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/portfolio/login/?next=/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[2]/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[2]/input")
        elem.send_keys("67854")
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "search for the client number"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
