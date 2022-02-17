import time

from selenium.webdriver.common.by import By

from pageobjects.Contact import Contact

from utilities import Excelutlis
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logger


class Test_001__DATADRIVENContact:
    # baseURL = "https://WEBO:C~T,e:3c5T]37QMD@webo.dev/dallcon-new/"
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testdata/contactusdata.xlsx"

    logger = Logger.logi()

    # def test_contactpagetitle_ndd(self, setup):
    #     self.logger.info("***** Test_002_Login ******")
    #     self.logger.info("** Verifying Contact Us Page title **")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.driver.find_element(By.LINK_TEXT, "Contact Us").click()
    #     time.sleep(4)
    #
    #     captured_title = self.driver.title
    #
    #     if captured_title == "Contact Us – Dallcon":
    #         self.logger.info("**Verified Contact Page Title**")
    #         assert True
    #         self.driver.close()
    #     else:
    #
    #         self.driver.save_screenshot(".\\screenshots\\" + "test_contactpagetitle.png")
    #         self.driver.close()
    #         self.logger.info("** SOORY Contact Page Unverified**")
    #         assert False

    def test_fillfeilds_ddt(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Contact Us").click()
        time.sleep(4)
        self.logger.info("**Entering Data on the Contact Form**")

        self.contact_obj = Contact(self.driver)
        self.row = Excelutlis.rowcount(self.path, 'Sheet1')

        # lst_status = []

        for r in range(2, self.row + 1):

            self.fullname = Excelutlis.readdata(self.path, 'Sheet1', r, 1)
            self.company = Excelutlis.readdata(self.path, 'Sheet1', r, 2)
            self.email = Excelutlis.readdata(self.path, 'Sheet1', r, 3)
            self.phone = Excelutlis.readdata(self.path, 'Sheet1', r, 4)
            self.knewhow = Excelutlis.readdata(self.path, 'Sheet1', r, 5)
            self.message = Excelutlis.readdata(self.path, 'Sheet1', r, 6)
            # self.result = Excelutlis.readdata(self.path, 'Sheet1', r, 7)

            self.contact_obj.fullName(self.fullname)
            self.contact_obj.companyName(self.company)
            self.contact_obj.emailAddress(self.email)
            self.contact_obj.phoneNumber(self.phone)
            self.contact_obj.foundUs(self.knewhow)
            self.contact_obj.message(self.message)
            self.contact_obj.clickExpert()
            time.sleep(4)

            try:
                succesful_message = self.driver.find_element_by_xpath(
                    "//div[normalize-space()='Thanks for submitting your enquiry, we will get back to you shortly!']")

                if succesful_message.text == "Thanks for submitting your enquiry, we will get back to you shortly!":
                    Excelutlis.savefile(self.path, 'Sheet1', r, 7, "TEST PASSED")

            except:
                Excelutlis.savefile(self.path, 'Sheet1', r, 7, "TEST FAILED")
                self.driver.save_screenshot(".\\screenshots\\" + "test_fillfeilds_ddt.png")


            self.driver.find_element(By.XPATH,"//nav[@id='site-navigation']//a[normalize-space()='Contact Us']").click()

        self.driver.close()

