import allure
from selenium.webdriver.common.by import By
from Web.FrameWork.Locators.SignupLocators import SignupLocators
from Web.FrameWork.Pages.SigninPage import SigninPage
from Web.FrameWork.Locators.SigninLocators import SigninLocators


class SignupPage(SigninPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.uname_txt_box = SigninLocators.user_name_id
        self.password_box = SigninLocators.password_id
        self.fname_txt_box = SignupLocators.first_name_id
        self.lname_txt_box = SignupLocators.last_name_id
        self.confirmPass_box = SignupLocators.confirm_pass_id
        self.signupButton = SignupLocators.button_signup

    @allure.step("Enter firstName as {1}")
    def enter_fname(self, fname):
        self.driver.find_element(By.ID, self.fname_txt_box).clear()
        self.driver.find_element(By.ID, self.fname_txt_box).send_keys(fname)

    @allure.step("Enter lastName as {1}")
    def enter_lname(self, lname):
        self.driver.find_element(By.ID, self.lname_txt_box).clear()
        self.driver.find_element(By.ID, self.lname_txt_box).send_keys(lname)

    @allure.step("Enter userName as {1}")
    def enter_unames(self, uname):
        self.enter_uname(uname)

    @allure.step("Enter password as {1}")
    def enter_passwords(self, password):
        self.enter_password(password)

    @allure.step("Enter confirmed password as {1}")
    def enter_confirmPass(self, confirmPass):
        self.driver.find_element(By.ID, self.confirmPass_box).clear()
        self.driver.find_element(By.ID, self.confirmPass_box).send_keys(confirmPass)

    @allure.step("Click on signup button")
    def click_signup(self):
        self.driver.find_element_by_xpath(self.signupButton).is_enabled()
