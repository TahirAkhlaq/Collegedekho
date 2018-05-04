from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.home.login_page import LoginPage
import pytest
from selenium.webdriver import ActionChains
import time

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://www.collegedekho.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        ele2 = driver.find_element_by_tag_name("h1").text
        print("The Tag Value is : ",ele2)
        driver.find_element_by_xpath("//a[@title='Engineering Colleges in India']").click()
        EnggElement = driver.find_element_by_tag_name("h1").text
        print("Engineer College Tag value is :", EnggElement)
        driver.find_element_by_xpath("//a[@title='IIT Delhi (IITD), Delhi'][contains(text(),'IIT Delhi (IITD), Delhi')]").click()
        CollegeElement = driver.find_element_by_tag_name("h1").text
        print("College Tag Value is :",CollegeElement)


        driver.quit()




