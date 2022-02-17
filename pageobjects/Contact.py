from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select


class Contact:
    textbox_fullname_id = "fullname"
    textbox_company_id = "field[30]"
    textbox_email_id = "email"
    textbox_phone_id = "phone"
    dropdown_where_id = "field[45]"
    textarea_message_id = "field[26]"
    button_expertalk_xpath = "//button[@id='_form_27_submit']"
    button_contactus_link = "Contact Us"

    def __init__(self, driver):
        self.driver = driver

    def fullName(self, name):
        self.driver.find_element_by_id(self.textbox_fullname_id).clear()
        self.driver.find_element_by_id(self.textbox_fullname_id).send_keys(name)

    def companyName(self, company):
        self.driver.find_element_by_id(self.textbox_company_id).clear()
        self.driver.find_element_by_id(self.textbox_company_id).send_keys(company)

    def emailAddress(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def phoneNumber(self, phone):
        self.driver.find_element_by_id(self.textbox_phone_id).clear()
        self.driver.find_element_by_id(self.textbox_phone_id).send_keys(phone)

    def foundUs(self, x):
        z = self.driver.find_element_by_id(self.dropdown_where_id)
        a = Select(z)
        a.select_by_index(x)

    def message(self, message):
        self.driver.find_element_by_id(self.textarea_message_id).clear()
        self.driver.find_element_by_id(self.textarea_message_id).send_keys(message)

    def clickExpert(self):
        self.driver.find_element(By.XPATH, self.button_expertalk_xpath).click()

    def clickContactus(self):

        self.driver.find_element(By.LINK_TEXT, self.button_contactus_link).click()
