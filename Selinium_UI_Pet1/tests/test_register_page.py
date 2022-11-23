import time
import pytest
from pages.register_page import NewUser


@pytest.mark.smoke_test
def test_go_to_main_page(browser):
    link = "http://34.141.58.52:8080/#/register"
    main_page = NewUser(browser, link)
    main_page.open()
    main_page.go_to_main_page()

@pytest.mark.xfail
def test_go_to_login(browser):
    link = "http://34.141.58.52:8080/#/register"
    page = NewUser(browser, link)
    page.open()
    page.register_and_delete_profile()
    time.sleep(3)
