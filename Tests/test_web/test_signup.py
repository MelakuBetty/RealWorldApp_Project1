from Web.FrameWork.Base.base import Base
from Web.FrameWork.Locators.SignupLocators import SignupLocators
from Web.FrameWork.Utils.Test_utils import sign_up
import allure
from Web.FrameWork.Utils.Assert import *
import pytest


@pytest.mark.usefixtures('init_driver_signup')
class TestSignup(Base):

    @pytest.mark.sanity
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' valid signup credentials")
    def test_signup_success(self):

        """Test signup correctly"""
        sign_up(self, "yuval", "usher", "yuvi", "123456", "123456")
        assertion(self, SignupLocators.signin_logo, SignupLocators.txt_logo)

    @pytest.mark.regression
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid first name credentials")
    def test_signup_firstName_Null(self):

        """Test signup incorrectly"""
        sign_up(self, "", "usher", "yuvi", "123456", "123456")
        assertion_buttons(self,SignupLocators.button_signup)
        assertion(self, SignupLocators.signin_logo, SignupLocators.txt_logo)

    @pytest.mark.regression
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid last name credentials")
    def test_signup_lastName_Null(self):

        """Test signup incorrectly"""
        sign_up(self, "yuval", "", "yuvi", "123456", "123456")
        assertion_buttons(self, SignupLocators.button_signup)
        assertion(self, SignupLocators.signin_logo, SignupLocators.txt_logo)

    @pytest.mark.regression
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid user name credentials")
    def test_signup_userName_Null(self):

        """Test signup incorrectly"""
        sign_up(self, "yuval", "usher", "", "123456", "123456")
        assertion_buttons(self, SignupLocators.button_signup)


    @pytest.mark.regression
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid signup credentials")
    def test_signup_password_Null(self):

        """Test signup incorrectly"""
        sign_up(self, "yuval", "usher", "yuvi", "", "123456")
        assertion_buttons(self, SignupLocators.button_signup)


    @pytest.mark.regression
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid signup credentials")
    def test_signup_confirmpassword_Null(self):

        """Test signup incorrectly"""
        sign_up(self, "yuval", "usher", "yuvi", "123456", "")
        assertion_buttons(self,SignupLocators.button_signup)

    @pytest.mark.sanity
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid signup credentials")
    def test_signup_fields_Null(self):

        """Test signup incorrectly"""
        sign_up(self, "", "", "", "", "")
        assertion_buttons(self,SignupLocators.button_signup)
