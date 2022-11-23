from .locators import RegisterPageLocators
from .base_page import BasePage


class NewUser(BasePage):

    def go_to_main_page(self):
        main_page = self.browser.find_element(*RegisterPageLocators.LOGO)
        main_page.click()

    def register_and_delete_profile(self):
        register_email = self.browser.find_element(*RegisterPageLocators.LOGIN_LINK)
        register_email.send_keys('qwertyio@gmail.ru')
        register_password = self.browser.find_element(*RegisterPageLocators.PASSWORD_LINK)
        register_password.send_keys("2734322a")
        register_password = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        register_password.send_keys("2734322a")
        btn_submit = self.browser.find_element(*RegisterPageLocators.BTN_SUBMIT)
        btn_submit.submit()
        delete_profile = self.browser.find_element(*RegisterPageLocators.DELETE_BTN)
        delete_profile.click()
        yes_delete = self.browser.find_element(*RegisterPageLocators.BTN_YES_DELETE)
        yes_delete.click()
