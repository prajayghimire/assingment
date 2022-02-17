import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.Contact import Contact
from random import randrange
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logger


class Test_002__Contact:
    # baseURL = "https://WEBO:C~T,e:3c5T]37QMD@webo.dev/dallcon-new/"
    baseURL = ReadConfig.getApplicationURL()

    logger = Logger.logi()

    # link_contactUs_xpath =
    def test_homepagetitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        home_title = self.driver.title

        if home_title == "Dallcon":
            assert True
            self.driver.close()
            self.logger.info("This is Home page")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.info("** SOORY Contact Page Unverified**")
            assert False

    def test_contactpagetitle(self, setup):
        self.logger.info("***** Test_002_Contact ******")
        self.logger.info("** Verifying Contact Us Page title **")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Contact Us").click()
        time.sleep(4)

        captured_title = self.driver.title

        if captured_title == "Contact Us – Dallcon":
            self.logger.info("**Verified Contact Page Title**")
            assert True
            self.driver.close()
        else:

            self.driver.save_screenshot(".\\screenshots\\" + "test_contactpagetitle.png")
            self.driver.close()
            self.logger.info("** SOORY Contact Page Unverified**")
            assert False

    def test_countlinks(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Contact Us").click()
        time.sleep(4)
        self.links = self.driver.find_elements(By.TAG_NAME, "a")
        print(len(self.links))

        for x in self.links:
            print(x.text)

        self.driver.close()

    def test_fillfeilds(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Contact Us").click()
        time.sleep(4)
        self.logger.info("**Entering Data on the Contact Form**")
        self.contact_obj = Contact(self.driver)
        self.contact_obj.fullName("tes Huty")
        self.contact_obj.companyName("WEBO")
        self.contact_obj.emailAddress("xyz@gmaile.com")
        self.contact_obj.phoneNumber("9804383838")
        x = randrange(11)
        self.contact_obj.foundUs(x)
        self.contact_obj.message("NOpe")
        self.contact_obj.clickExpert()
        time.sleep(4)
        try:

            succesful_message = self.driver.find_element_by_xpath(
                "//div[normalize-space()='Thanks for submitting your enquiry, we will get back to you shortly!']")

            if succesful_message.text == "Thanks for submitting your enquiry, we will get back to you shortly!":
                assert True
                self.logger.info("**Your data Summited**")
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\" + "test_fillfeilds.png")
                self.logger.error("**Invalid data entered **")
                assert False
                self.driver.close()

        except:

            self.logger.error("failed")
            self.driver.save_screenshot(".\\screenshots\\" + "test_fillfeilds.png")
            self.driver.close()
            assert False


