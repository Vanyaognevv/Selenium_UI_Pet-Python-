from .base_page import BasePage
from pages.locators import LoginPageLocators, ProfilePageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('Qachecker@gmail.ru')

        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys("2734322a")

        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()

class ProfilePage(BasePage):
    def add_new_pet(self):
        button_plus = self.browser.find_element(*ProfilePageLocators.PLUS_BUTTON)
        button_plus.click()

        name_pet = self.browser.find_element(*ProfilePageLocators.NAME_PET)
        name_pet.send_keys('Повторяха')

        pet_type = self.browser.find_element(*ProfilePageLocators.PET_TYPE)
        pet_type.click()

        pet_type_perrot = self.browser.find_element(*ProfilePageLocators.PET_TYPE_DOG)
        pet_type_perrot.click()

        age = self.browser.find_element(*ProfilePageLocators.AGE)
        age.send_keys(3)

        gender_type = self.browser.find_element(*ProfilePageLocators.GENDER_TYPE)
        gender_type.click()

        gender_male = self.browser.find_element(*ProfilePageLocators.GENDER_MALE)
        gender_male.click()

        button_submit_new_pet = self.browser.find_element(*ProfilePageLocators.BUTTON_SUBMIT_NEW_PET)
        button_submit_new_pet.click()

        button_choose = self.browser.find_element(*ProfilePageLocators.BUTTON_CHOOSE)
        button_choose.click()

