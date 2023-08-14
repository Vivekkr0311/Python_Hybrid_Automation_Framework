import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()

    logger = LogGen.logGen()

    logger.info("********** Test_001 Login ***********")
    def test_homePageTitle(self, setup):
        self.logger.info("********** Verifying Home Page Title ***********")

        # Here, setup is fixture which is used to launch the webdriver.
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Title Validation Passed ***********")
        else:
            self.driver.save_screenshot(
                "/Users/vivek/PycharmProjects/Python_Hybrid_Automation_Framework/Screenshots/" + "test_HomePageTitle.png")
            assert False
            self.driver.close()
            self.logger.error("********** Title Validation Failed ***********")

    def test_login(self, setup):
        self.logger.info("********** Verifying Log In Test Case ***********")

        # Here, setup is fixture which is used to launch the webdriver.
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginPage_Object = LoginPage(self.driver)
        self.loginPage_Object.setUserName(self.username)
        self.loginPage_Object.setPassword(self.password)
        self.loginPage_Object.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********** Test Log In Validation Passed ***********")
        else:
            self.driver.save_screenshot(
                "/Users/vivek/PycharmProjects/Python_Hybrid_Automation_Framework/Screenshots/" + "test_HomePageTitle.png")
            assert False
            self.driver.close()
            self.logger.error("********** Test Log in Validation Failed ***********")