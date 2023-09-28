from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver=driver


    email_address_box_xpath= "//input[@id='input-email']"
    password_box_xpath ="//input[@id='input-password']"
    login_button_xpath ="//input[@value='Login']"
    warning_message_xpath="//div[@class='alert alert-danger alert-dismissible']"


    def enter_email_id(self,emailid):
        self.driver.find_element(By.XPATH,self.email_address_box_xpath).click()
        self.driver.find_element(By.XPATH,self.email_address_box_xpath).clear()
        self.driver.find_element(By.XPATH,self.email_address_box_xpath).send_keys(emailid)

    def enter_password(self,pwd):
        self.driver.find_element(By.XPATH,self.password_box_xpath).click()
        self.driver.find_element(By.XPATH,self.password_box_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_box_xpath).send_keys(pwd)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def warning_message_for_invalid_email(self):
        return self.driver.find_element(By.XPATH,self.warning_message_xpath).is_displayed()


    







    