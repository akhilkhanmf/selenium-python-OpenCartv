import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from PageObject.AccountPage import AccountPage


@pytest.mark.usefixtures("setup")
class TestLogin():
    def test_login_with_valid_credentials(self):
        hp=HomePage(self.driver)
        hp.select_my_account()
        hp.select_login()
        lp=LoginPage(self.driver)
        lp.enter_email_id("podcod@gmail.com")
        lp.enter_password("12345678")
        lp.click_login_button()
        ap=AccountPage(self.driver)
        assert ap.edit_your_account_information_option()
        


    def test_login_with_invalid_email_valid_password(self):
        
        hp=HomePage(self.driver)
        hp.select_my_account()
        hp.select_login()
        lp=LoginPage(self.driver)
        lp.enter_email_id(generate_random_email_with_timestamp())
        lp.enter_password("12345678")
        lp.click_login_button()
        assert lp.warning_message_for_invalid_email()

    def test_login_with_valid_email_invalid_password(self):
        
        hp=HomePage(self.driver)
        hp.select_my_account()
        hp.select_login()
        lp=LoginPage(self.driver)
        lp.enter_email_id("podcod@gmail.com")
        lp.enter_password("123")
        lp.click_login_button()
        assert lp.warning_message_for_invalid_email()
        
    def test_login_without_credentials(self):
        
        hp=HomePage(self.driver)
        hp.select_my_account()
        hp.select_login()
        lp=LoginPage(self.driver)
        lp.enter_email_id("")
        lp.enter_password("")
        lp.click_login_button()
        assert lp.warning_message_for_invalid_email()
        

def generate_random_email_with_timestamp():
        current_time = datetime.datetime.now()

    # Format the current time as part of the email address
        formatted_time = current_time.strftime("%Y%m%d%H%M%S")

    # Generate the email address
        email_address = f"podcode_{formatted_time}@example.com"
        return email_address
    






    
    
