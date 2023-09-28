from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from PageObject.HomePage import HomePage
from PageObject.SearchPage import SearchPage
import datetime


@pytest.mark.usefixtures("setup")
class TestSearch():
        def test_search_for_valid_product(self):
                hp=HomePage(self.driver)
                hp.enter_a_product_on_search_box("HP")
                hp.click_on_the_search_button()
                sp=SearchPage(self.driver)
                assert sp.display_status_of_hp_product()

        def test_search_for_invalid_product(self):
                hp=HomePage(self.driver)
                hp.enter_a_product_on_search_box("Honda")
                hp.click_on_the_search_button()
                sp=SearchPage(self.driver)
                assert sp.display_status_of_invlaid_product()

        def test_serach_for_without_entering_product(self):
                hp=HomePage(self.driver)
                hp.enter_a_product_on_search_box("")
                hp.click_on_the_search_button()
                sp=SearchPage(self.driver)
                assert sp.display_status_of_invlaid_product()
                                

