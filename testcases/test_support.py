
#Ths is of the Webo official page later relaized there is a recaptcha.

# import time
#
# import pytest
# from selenium import webdriver
# from pageobjects.Support import Support
# from random import randrange
#
#
# class Test_001__Support:
#     # baseURL =
#
#     link_support_xpath = "//li[@class='menu-item menu-item-type-post_type menu-item-5279']//a[normalize-space()='SUPPORT']"
#
#     def test_supportpagetitle(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.baseURL)
#         self.driver.find_element_by_xpath(self.link_support_xpath).click()
#         time.sleep(5)
#
#         captured_title = self.driver.title
#
#         self.driver.close()
#
#         if captured_title == "Customer Support - WEBO Digital":
#
#             assert True
#         else:
#             assert False
#
#     def test_fillFields(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.baseURL)
#         self.driver.find_element_by_xpath(self.link_support_xpath).click()
#         time.sleep(5)
#         self.login_obj = Support(self.driver)
#         self.login_obj.setFirstName("Prajay")
#         self.login_obj.setLastName("Ghimire")
#         self.login_obj.email("chukedai309@gmail.com")
#         self.login_obj.issue("Automation Working")
#         x = randrange(3)
#         self.login_obj.priority(x)
#         self.login_obj.detailedissue("So Far So good")
#         self.login_obj.upload("D:/pic/test1.xlsx")
#         self.login_obj.CreateSupportButton()
