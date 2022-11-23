from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LiNK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    NEXT_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[3]/span')
    LAST_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[4]/span')
    SEARCH_NAME = (By.XPATH, '//*[@id="petName"]')
    FILTER_BY_TYPE = (By.CSS_SELECTOR, "#typesSelector")
    DOG = (By.XPATH, '//*[@id="pv_id_2_0"]')
    COMMENTS = (By.XPATH, '//*[@id="app"]/main/div[2]/div/div/div[3]/form/div/div/div[2]/div[1]')
    DETAILS = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button/span')
    DETAILS_MY_PET = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button/span')
    PHOTO = (By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/span/div')
    LOGO = (By.XPATH, '//*[@id="app"]/header/div/div/img')
    REGISTER_PAGE = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a')

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, 'p-button-label')

class RegisterPageLocators:
    REGISTER_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(2) > a > span")
    DELETE_BTN = (By.CSS_SELECTOR, "#app > main > div > div > div.p-dataview-header > div > div:nth-child(2) > button")
    BTN_YES_DELETE = (By.CSS_SELECTOR,
                      "body > div.p-confirm-popup.p-component.p-ripple-disabled > div.p-confirm-popup-footer > "
                      "button.p-button.p-component.p-confirm-popup-accept.p-button-sm > span")
    LOGIN_LINK = (By.XPATH, '//*[@id="login"]')
    PASSWORD_LINK = (By.XPATH, '//*[@id="password"]/input')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="confirm_password"]/input')
    LOGIN_BTN = (By.XPATH, '//*[@id="pv_id_12_content"]/div/form/div[4]/button')
    LOGO = (By.XPATH, '//*[@id="app"]/header/div/div/img')
    BTN_SUBMIT = (By.CLASS_NAME, 'p-button-label')

class ProfilePageLocators:
    PLUS_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button/span[1]')
    NAME_PET = (By.XPATH, '//*[@id="name"]')
    PET_TYPE = (By.XPATH, '//*[@id="typeSelector"]')
    GENDER_TYPE = (By.XPATH, '//*[@id="genderSelector"]')
    AGE = (By.XPATH, '//*[@id="age"]/input')
    BUTTON_SUBMIT_NEW_PET = (By.CSS_SELECTOR,
                      '#app > main > div > div > form > div > div.p-card-body > div.p-card-footer > '
                      'button.p-button.p-component.p-button-success > span.p-button-label')
    PET_TYPE_DOG = (By.XPATH, '//*[@id="pv_id_2_1"]')
    GENDER_MALE = (By.XPATH, '//*[@id="pv_id_3_0"]')
    BUTTON_CHOOSE = (By.CSS_SELECTOR, "#app > main > div > div > div:nth-child(2) > "
                                      "div.col-12.justify-content-center.flex > div > span > span.p-button-label")







