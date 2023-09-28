from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self,driver):
        self.driver=driver

    valid_product_xpath ="//a[normalize-space()='HP LP3065']"
    invalid_product_xpath="//input[@id='button-search']/following-sibling::p"


    def display_status_of_hp_product(self):
        return self.driver.find_element(By.XPATH,self.valid_product_xpath).is_displayed()


    def display_status_of_invlaid_product(self):
        return self.driver.find_element(By.XPATH,self.invalid_product_xpath).is_displayed()