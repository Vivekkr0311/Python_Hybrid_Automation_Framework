from selenium import webdriver

class LoginPage:
    email_field = "//input[@id='Email']"
    password_field = "//input[@id='Password']"
    login_button = "//button[@type='submit']"
    logout_button = "//a[@href='/logout']"

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        # Using xpath
        # self.driver.find_element_by_xpath(self.email_field).clear()
        # self.driver.find_element_by_xpath(self.email_field).send_keys(username)

        # Using id
        self.driver.find_element_by_id(self.text_username_id).clear()
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setPassword(self, password):
        # Using xpath
        # self.driver.find_element_by_xpath(self.password_field).clear()
        # self.driver.find_element_by_xpath(self.password_field).send_keys(password)

        # Using id
        self.driver.find_element_by_id(self.text_username_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        # Using xpath
        self.driver.find_element_by_xpath(self.login_button).click()

    def clickLogout(self):
        # Using link text
        self.driver.find_element_by_linktext(self.link_logout_linktext).click()

        # # Using xpath
        # self.driver.find_element_by_xpath(self.logout_button).click()