import time
import unittest2
from ddt import file_data, ddt
from selenium import webdriver
from function_page.register_page import RegisterPage

@ddt
class TestRegister(unittest2.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        # time.sleep(1)
        self.driver.quit()

    @file_data("../data.yaml")
    def test_register(self, username_date, password_date, password_confirm_date, phone_number_date, email_date):
        lp = RegisterPage(self.driver)
        lp.register_usr(username_date, password_date, password_confirm_date, phone_number_date, email_date)
        time.sleep(5)


