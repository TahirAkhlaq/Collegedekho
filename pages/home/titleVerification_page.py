import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class TitleVerificationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
       # self.nav = NavigationPage(driver)

    #Locators
    _homepagetitle = "//h1[contains(text(),'Find Top Colleges, Discover Courses & Exams, Get A')]"

