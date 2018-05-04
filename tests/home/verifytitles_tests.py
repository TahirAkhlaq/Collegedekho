from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.home.titleVerification_page import TitleVerificationPage
from selenium import webdriver


class VerifyTitles(unittest.TestCase):


    def VerifyTitles(self):
        driver = webdriver.Firefox()
        baseURL = "https://www.collegedekho.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        self.tp = TitleVerificationPage(driver)
        result= self.tp.verifyHomePageTitle()
        assert result == True
