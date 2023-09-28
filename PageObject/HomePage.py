from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self,driver):
        self.driver = driver


    search_box_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    click_on_the_my_account_icon_xpath ="//a[@title='My Account']"
    click_on_the_login_icon_xpath="//a[normalize-space()='Login']"
    click_on_the_register_icon_xpath="//a[normalize-space()='Register']"

    def enter_a_product_on_search_box(self,product_name):
        self.driver.find_element(By.XPATH,self.search_box_xpath).click()
        self.driver.find_element(By.XPATH,self.search_box_xpath).clear()
        self.driver.find_element(By.XPATH,self.search_box_xpath).send_keys(product_name)

    def click_on_the_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def select_my_account(self):
        self.driver.find_element(By.XPATH,self.click_on_the_my_account_icon_xpath).click()

    def select_login(self):
        self.driver.find_element(By.XPATH,self.click_on_the_login_icon_xpath).click()

    def select_register(self):
        self.driver.find_element(By.XPATH,self.click_on_the_register_icon_xpath).click()

    

    

