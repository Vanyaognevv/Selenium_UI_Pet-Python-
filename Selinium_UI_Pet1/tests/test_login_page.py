import time
from pages.login_page import LoginPage
import pytest

@pytest.mark.regression_test
def test_go_to_login(browser):
    link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    time.sleep(3)
