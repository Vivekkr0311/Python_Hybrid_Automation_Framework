import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()

    def test_homePageTitle(self, setup):
        # Here, setup is fixture which is used to launch the webdriver.
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
           assert True
        else:
            assert False

    def test_login(self, setup):
        # Here, setup is fixture which is used to launch the webdriver.
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginPage_Object = LoginPage(self.driver)
        self.loginPage_Object.setUserName(self.username)
        self.loginPage_Object.setPassword(self.password)
        self.loginPage_Object.clickLogin()

        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
           assert True
        else:
            assert False