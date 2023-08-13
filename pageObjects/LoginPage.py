from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    email_field_xpath = "//input[@id='Email']"
    password_field_xpath = "//input[@id='Password']"
    login_button_xpath = "//button[@type='submit']"
    logout_button_xpath = "//a[@href='/logout']"

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        # Using xpath
        self.driver.find_element(By.XPATH, self.email_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_field_xpath).send_keys(username)

        # Using id
        # self.driver.find_element(By.ID, self.text_username_id).clear()
        # self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def setPassword(self, password):
        # Using xpath
        self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

        # Using id
        # self.driver.find_element(By.ID, self.text_username_id).clear()
        # self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        # Using xpath
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def clickLogout(self):
        # Using link text
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

        # # Using xpath
        # self.driver.find_element_by_xpath(self.logout_button).click()