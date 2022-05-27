import allure
from selenium.webdriver.common.by import By
from Web.FrameWork.Locators.SigninLocators import SigninLocators


class SigninPage:

    def __init__(self, driver):
        self.driver = driver
        self.uname_txt_box = SigninLocators.user_name_id
        self.password_box = SigninLocators.password_id
        self.signin_button = SigninLocators.signin_button

    @allure.step("Enter userName as {1}")
    def enter_uname(self, uname):
        self.driver.find_element(By.ID, self.uname_txt_box).clear()
        self.driver.find_element(By.ID, self.uname_txt_box).send_keys(uname)

    @allure.step("Enter password as {1}")
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_box).clear()
        self.driver.find_element(By.ID, self.password_box).send_keys(password)

    @allure.step("Click on signin button")
    def click_signin(self):
        self.driver.find_element(By.XPATH, self.signin_button).is_enabled()
