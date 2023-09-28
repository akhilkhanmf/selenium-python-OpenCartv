
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from PageObject.HomePage import HomePage
from PageObject.RegisterPage import RegisterPage

from PageObject.AccountSuccessPage import AccountSuccessPage
from Tests.test_login import generate_random_email_with_timestamp

@pytest.mark.usefixtures("setup")
class TestRegister():
    def test_register_with_mandatory_fields(self):
        
        hp=HomePage(self.driver)
        hp.select_my_account()
        hp.select_register()
        rp=RegisterPage(self.driver)
        rp.enter_frist_name("pod")
        rp.enter_last_name("cod584125")
        rp.enter_email_id(generate_random_email_with_timestamp())
        rp.enter_telephone_number("7161616564161")
        rp.enter_password("789456")
        rp.enter_confirm_password("789456")
        rp.checkbox_agree()
        rp.click_continue_button()
        asp=AccountSuccessPage(self.driver)
        assert asp.account_creation_message()

    def test_register_with_all_fields(self):

        hp=HomePage(self.driver)
        hp.select_my_account()
        hp.select_register()
        rp=RegisterPage(self.driver)
        rp.enter_frist_name("pod")
        rp.enter_last_name("cod125854")
        rp.enter_email_id(generate_random_email_with_timestamp())
        rp.enter_telephone_number("7161616564161")
        rp.enter_password("789456")
        rp.enter_confirm_password("789456")
        rp.click_normalize_field()
        rp.checkbox_agree()
        rp.click_continue_button()
        asp=AccountSuccessPage(self.driver)
        assert asp.account_creation_message()
        


    def test_register_existing_account(self):

        hp=HomePage(self.driver)
        hp.select_my_account()
        hp.select_register()
        rp=RegisterPage(self.driver)
        rp.enter_frist_name("pod")
        rp.enter_last_name("cod1258584")
        rp.enter_email_id("podcod@gmail.com")
        rp.enter_telephone_number("7161616564161")
        rp.enter_password("987654")
        rp.enter_confirm_password("987654")
        rp.click_normalize_field()
        rp.checkbox_agree()
        rp.click_continue_button()
        assert rp.appear_warning_message_existing_account()
        

    def test_register_empty_field(self):

        hp=HomePage(self.driver)
        hp.select_my_account()
        hp.select_register()
        rp=RegisterPage(self.driver)
        rp.checkbox_agree()
        rp.click_continue_button()
        rp.appear_warning_privacy_plicy_message_xpath()
        rp.appear_warning_firstname_xpath()
        rp.appear_warning_message_last_name()
        rp.appear_warning_email_xpath()
        rp.appear_warning_telephone_xpath()
        rp.appear_warning_password_xpathe()


    def generate_random_email_with_timestamp():
        current_time = datetime.datetime.now()

    # Format the current time as part of the email address
        formatted_time = current_time.strftime("%Y%m%d%H%M%S")

    # Generate the email address
        email_address = f"podcode_{formatted_time}@example.com"
        return email_address


        
        

