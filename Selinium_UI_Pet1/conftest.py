import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome('C:\\Driver\\chromedriver.exe')
    yield browser
    browser.quit()
