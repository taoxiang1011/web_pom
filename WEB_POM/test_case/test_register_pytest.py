import time
import pytest
from ddt import file_data, ddt
from selenium import webdriver

from common.read_data import read_data
from function_page.register_page import RegisterPage
excl_dir = r"./data/data.xlsx"
sheet_name = "register"

class TestRegister:
    def setup(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self) -> None:
        # time.sleep(1)
        self.driver.quit()


    @pytest.mark.parametrize("caseinfo", read_data(excl_dir, sheet_name))
    def test_register(self, caseinfo):
        username_date, password_date, password_confirm_date, phone_number_date, email_date = caseinfo
        lp = RegisterPage(self.driver)
        lp.register_usr(username_date, password_date, password_confirm_date, phone_number_date, email_date)
        time.sleep(2)


if __name__ == '__main__':
    pytest.main()
