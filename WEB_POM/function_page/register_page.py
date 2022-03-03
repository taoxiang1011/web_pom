from selenium.webdriver.common.by import By
from base.base_page import BasePage

class RegisterPage(BasePage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    password_confirm = (By.NAME, "userpassword2")
    phone_number = (By.NAME, "mobile_phone")
    email = (By.NAME, "email")

    def register_usr(self, username_date, password_date, password_confirm_date, phone_number_date, email_date):
        """用户注册功能"""
        self.get("http://127.0.0.1/index.php?m=user&c=public&a=reg")
        self.send_keys(self.username, username_date)
        self.send_keys(self.password, password_date)
        self.send_keys(self.password_confirm, password_confirm_date)
        self.send_keys(self.phone_number, phone_number_date)
        self.send_keys(self.email, email_date)








