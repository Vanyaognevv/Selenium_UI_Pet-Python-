from .locators import MainPageLocators, RegisterPageLocators
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):

    def go_to_register_page(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_PAGE)
        register_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LiNK)
        login_link.click()

    def search_by_name(self):
        nickname = self.browser.find_element(*MainPageLocators.SEARCH_NAME)
        nickname.send_keys('Vivi')
        button_logo = self.browser.find_element(*MainPageLocators.LOGO)
        button_logo.click()

    def filter_by_type(self):
        button_type = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        button_type.click()
        dog = self.browser.find_element(*MainPageLocators.DOG)
        dog.click()

    def details_button(self):
        button_details = self.browser.find_element(*MainPageLocators.DETAILS)
        button_details.click()
        comments = self.browser.find_element(*MainPageLocators.COMMENTS)
        comments.send_keys('Good nice')

    def next_page_pet(self):
        button_next = self.browser.find_element(*MainPageLocators.NEXT_PAGE)
        button_next.click()

    def last_page_pet(self):
        last_page = self.browser.find_element(*MainPageLocators.LAST_PAGE)
        last_page.click()

    def look_photo(self):
        button_details = self.browser.find_element(*MainPageLocators.DETAILS_MY_PET)
        button_details.click()
        choose_photo = self.browser.find_element(*MainPageLocators.PHOTO)
        choose_photo.click()
