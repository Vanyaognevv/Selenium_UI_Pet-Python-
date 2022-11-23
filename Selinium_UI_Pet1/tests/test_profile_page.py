from pages.profile_page import LoginPage, ProfilePage
import time
import pytest

@pytest.mark.regression_test
def test_add_new_pet(browser):
    link= 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    time.sleep(3)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.add_new_pet()
    time.sleep(3)

