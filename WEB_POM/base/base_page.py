from selenium import webdriver
from common.logger import getlog


class BasePage:
    def __init__(self, driver):
        self.log = getlog()
        self.driver = driver


    def get(self, url):
        """打开网页"""
        self.driver.get(url)
        self.log.info("正在访问{}网址".format(url))


    def locator(self, args):
        """元素的定位"""
        self.log.info("正在定位{}".format(args))
        return self.driver.find_element(*args)


    def send_keys(self, args, value):
        """输入数据"""
        self.locator(args).send_keys(value)
        self.log.info("正在输入{}".format(value))


    def click(self, args):
        """点击操作"""
        self.locator(args).click()
        self.log.info("正在点击{}按钮".format(args))










