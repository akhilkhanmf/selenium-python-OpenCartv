from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterPage():
    def __init__(self,driver):
        self.driver = driver

    first_name_xpath = "//input[@id='input-firstname']"
    last_name_xpath = "//input[@id='input-lastname']"
    email_field_xpath="//input[@id='input-email']"
    telephone_field_xpath="//input[@id='input-telephone']"
    password_field_xpath = "//input[@id='input-password']"
    confirm_pwd_xpath="//input[@id='input-confirm']"
    agree_statement_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    normalize_space_xpath="//label[normalize-space()='Yes']"
    warning_existing_amount_message_xpath = "//div[@id='account-register']/div[1]"
    warning_privacy_plicy_message_xpath = "//div[@id='account-register']/div[1]"
    warning_firstname_xpath="//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    warning_lastname_xpath="//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    warning_email_xpath="//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    warning_telephone_xpath="//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    warning_password_xpath="//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"


    def enter_frist_name(self,fname):
        self.driver.find_element(By.XPATH,self.first_name_xpath).click()
        self.driver.find_element(By.XPATH,self.first_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.first_name_xpath).send_keys(fname)

    def enter_last_name(self,lname):
        self.driver.find_element(By.XPATH,self.last_name_xpath).click()
        self.driver.find_element(By.XPATH,self.last_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.last_name_xpath).send_keys(lname)

    def enter_email_id(self,ename):
        self.driver.find_element(By.XPATH,self.email_field_xpath).click()
        self.driver.find_element(By.XPATH,self.email_field_xpath).clear()
        self.driver.find_element(By.XPATH,self.email_field_xpath).send_keys(ename)

    def enter_telephone_number(self,tnum):
        self.driver.find_element(By.XPATH,self.telephone_field_xpath).click()
        self.driver.find_element(By.XPATH,self.telephone_field_xpath).clear()
        self.driver.find_element(By.XPATH,self.telephone_field_xpath).send_keys(tnum)

    def enter_password(self,pname):
        self.driver.find_element(By.XPATH,self.password_field_xpath).click()
        self.driver.find_element(By.XPATH,self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_field_xpath).send_keys(pname)

    def enter_confirm_password(self,cpname):
        self.driver.find_element(By.XPATH,self.confirm_pwd_xpath).click()
        self.driver.find_element(By.XPATH,self.confirm_pwd_xpath).clear()
        self.driver.find_element(By.XPATH,self.confirm_pwd_xpath).send_keys(cpname)

    def checkbox_agree(self):
        self.driver.find_element(By.XPATH,self.agree_statement_xpath).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath).click()

    def click_normalize_field(self):
        self.driver.find_element(By.XPATH,self.normalize_space_xpath).click()

    def appear_warning_message_existing_account(self):
        return self.driver.find_element(By.XPATH,self.warning_existing_amount_message_xpath).is_displayed()
    
    def appear_warning_privacy_plicy_message_xpath(self):
        return self.driver.find_element(By.XPATH,self.warning_privacy_plicy_message_xpath).is_displayed()
    
    def appear_warning_firstname_xpath(self):
        return self.driver.find_element(By.XPATH,self.warning_firstname_xpath).is_displayed()
    
    
    def appear_warning_message_last_name(self):
        return self.driver.find_element(By.XPATH,self.warning_lastname_xpath).is_displayed()
    
    def appear_warning_email_xpath(self):
        return self.driver.find_element(By.XPATH,self.warning_email_xpath).is_displayed()
    
    def appear_warning_telephone_xpath(self):
        return self.driver.find_element(By.XPATH,self.warning_telephone_xpath).is_displayed()
    
    def appear_warning_password_xpathe(self):
        return self.driver.find_element(By.XPATH,self.warning_password_xpath).is_displayed()
    



    



        





    




