from pages.main_page import MainPage
import pytest


@pytest.mark.regression_test
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.smoke_test
def test_go_to_register_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()

@pytest.mark.smoke_test
def test_search_by_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.search_by_name()

@pytest.mark.xfail
def test_filter_by_type(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_type()

@pytest.mark.smoke_test
def test_details_button(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.details_button()

@pytest.mark.functionality_test
def test_next_page_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.next_page_pet()

@pytest.mark.functionality_test
def test_last_page_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.last_page_pet()

@pytest.mark.functionality_test
def test_look_photo(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.look_photo()
