from Web.FrameWork.Base.base import Base
from Web.FrameWork.Locators.SigninLocators import SigninLocators
from Web.FrameWork.Utils.Test_utils import sign_in
from Web.FrameWork.Utils.Assert import *
import pytest
import allure

@pytest.mark.usefixtures('init_driver')
class TestSignin(Base):

    @pytest.mark.sanity
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' valid signin credentials")
    def test_signin_successfully(self):

        """ Test signin correctly"""
        sign_in(self, "yuvi", "123456")
        assertion(self, SigninLocators.massage, SigninLocators.txt)

    @pytest.mark.sanity
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' Null signin credentials")
    def test_signin_unsuccessfully(self):

        """ Test signin incorrectly Null"""
        sign_in(self, "", "")
        assertion_buttons(self, SigninLocators.signin_button)
        assertion(self, SigninLocators.empty_uname, SigninLocators.txt_error)

    @pytest.mark.sanity
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_signin_unsuccessfully1(self):

        """ Test signup incorrectly"""
        sign_in(self, "yovui", "123456")
        assertion(self, SigninLocators.invalid_user_pass, SigninLocators.txt_invalid)


    @pytest.mark.sanity
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_signin_unsuccessfully2(self):

        """ Test signup incorrectly"""
        sign_in(self, "yuvi", "2556")
        assertion(self, SigninLocators.invalid_user_pass, SigninLocators.txt_invalid)

    @pytest.mark.sanity
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_signin_unsuccessfully3(self):

        """ Test signup incorrectly"""
        sign_in(self, "yuyobiv", "12345689")
        assertion(self, SigninLocators.invalid_user_pass, SigninLocators.txt_invalid)
