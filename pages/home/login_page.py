import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
       # self.nav = NavigationPage(driver)

    # Locators
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):

        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyHomePageTitle(self):
        if " Find Top Colleges, Discover Courses & Exams, Get Admission In The College Best Fit For You" in self.getTitle():
            return True
        else:
            return False




