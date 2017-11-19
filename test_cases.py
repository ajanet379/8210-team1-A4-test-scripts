#Kyle Hampton Test Cases
# 3 Test Cases Included
# Add new donor, edit existing donor, and delete existing donor

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()


# Test Script 1 - Add New Donor
   def test_blog(self):
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
       assert "Logged In"
       time.sleep(5)
       driver.get("http://127.0.0.1:8000/donor/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div/div[3]/div/a/span").click()
       time.sleep(5)
       name = "John Smith"
       address = "1234 Pine Street"
       number = "987654"
       city = "Omaha"
       state = "Nebraska"
       zip = "68114"
       email = "jsmith@gmail.com"
       phone = "402-555-5555"
       elem = driver.find_element_by_id("id_name")
       elem.send_keys(name)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys(address)
       elem = driver.find_element_by_id("id_donor_number")
       elem.send_keys(number)
       elem = driver.find_element_by_id("id_city")
       elem.send_keys(city)
       elem = driver.find_element_by_id("id_state")
       elem.send_keys(state)
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys(zip)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email)
       elem = driver.find_element_by_id("id_cell_phone")
       elem.send_keys(phone)
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
       time.sleep(10)
       assert "Added New Donor"


       # Test Script 2 - Edit Existing Donor
       driver.get("http://127.0.0.1:8000/donor/")
       elem = driver.find_element_by_xpath("//*[@id='userTbl']/tbody/tr[2]/td[9]/a").click()
       time.sleep(5)
       name2 = "Jeffrey Smith"
       address2 = "4321 Elm Avenue"
       number2 = "555555"
       city2 = "Gretna"
       zip2 = "68102"
       email2 = "jeffreysmith@hotmail.com"
       elem = driver.find_element_by_id("id_name").clear()
       elem = driver.find_element_by_id("id_address").clear()
       elem = driver.find_element_by_id("id_donor_number").clear()
       elem = driver.find_element_by_id("id_city").clear()
       elem = driver.find_element_by_id("id_zipcode").clear()
       elem = driver.find_element_by_id("id_email").clear()
       time.sleep(5)
       elem = driver.find_element_by_id("id_name")
       elem.send_keys(name2)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys(address2)
       elem = driver.find_element_by_id("id_donor_number")
       elem.send_keys(number2)
       elem = driver.find_element_by_id("id_city")
       elem.send_keys(city2)
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys(zip2)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email2)
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
       time.sleep(10)
       assert "Edited Existing Donor"


       # Test Script 3 - Delete Existing Donor
       elem = driver.find_element_by_xpath("//*[@id='userTbl']/tbody/tr[2]/td[10]/a").click()
       time.sleep(5)
       alert = driver.switch_to_alert()
       alert.accept()
       time.sleep(10)
       assert "Delete Existing Donor"


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
