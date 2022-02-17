#Webo

# import time
# from random import randrange
# from selenium.webdriver.support.ui import Select
#
# from selenium import webdriver
#
#
# class Support:
#     # link_support_xpath="//li[@class='menu-item menu-item-type-post_type menu-item-5279']//a[normalize-space()='SUPPORT']"
#     textbox_firstname_id = "firstname-e8099656-fb5f-4123-a2bc-cb2ac477e28c"
#     textbox_lastname_id = "lastname-e8099656-fb5f-4123-a2bc-cb2ac477e28c"
#     textbox_email_id = "email-e8099656-fb5f-4123-a2bc-cb2ac477e28c"
#     textbox_issuetitle_xpath = "//input[@id='TICKET.subject-e8099656-fb5f-4123-a2bc-cb2ac477e28c']"
#     dropdown_priority_xpath = "//select[@id='TICKET.hs_ticket_priority-e8099656-fb5f-4123-a2bc-cb2ac477e28c']"
#     textbox_detailed_issue_xpath = "//textarea[@id='TICKET.content-e8099656-fb5f-4123-a2bc-cb2ac477e28c']"
#     upload_files_xpath = "//input[@id='TICKET.hs_file_upload-e8099656-fb5f-4123-a2bc-cb2ac477e28c']"
#     button_createticket_xpath = "//input[@value='SUBMIT TICKET']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # def clickSupport(self):
#     #     self.driver.find_element_by_xpath(self.link_support_xpath).click()
#
#     time.sleep(5)
#
#     def setFirstName(self, fname):
#         self.driver.find_element_by_id(self.textbox_firstname_id).clear()
#         self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(fname)
#
#     def setLastName(self, lname):
#         self.driver.find_element_by_id(self.textbox_lastname_id).clear()
#         self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lname)
#
#     def email(self, email):
#         self.driver.find_element_by_id(self.textbox_email_id).clear()
#         self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)
#
#     def issue(self, issues):
#         self.driver.find_element_by_xpath(self.textbox_issuetitle_xpath).clear()
#         self.driver.find_element_by_xpath(self.textbox_issuetitle_xpath).send_keys(issues)
#
#     def priority(self, x):
#         z = self.driver.find_element_by_xpath(self.dropdown_priority_xpath)
#         a = Select(z)
#         a.select_by_index(x)
#
#     def detailedissue(self, x):
#         self.driver.find_element_by_xpath(self.textbox_detailed_issue_xpath).clear()
#         self.driver.find_element_by_xpath(self.textbox_detailed_issue_xpath).send_keys(x)
#
#     def upload(self, file):
#         self.driver.find_element_by_xpath(self.upload_files_xpath).send_keys(file)
#
#     def CreateSupportButton(self):
#         self.driver.find_element_by_xpath(self.button_createticket_xpath).click()
