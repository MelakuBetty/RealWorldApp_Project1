import allure
import pytest
import requests


class TestLogin:

    # @pytest.mark.sanity
    # @pytest.mark.nightly_build
    # @pytest.mark.severity(pytest.allure.severity_level.NORMAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_incorrect_login(self):
        url = "http://localhost:3001/login"
        body = {"type":"LOGIN","username":"BettyM","password":"142536"}
        x = requests.post(url, data=body)
        assert x.status_code == 401
        assert x.elapsed.total_seconds() < 5

    # @pytest.mark.sanity
    # @pytest.mark.nightly_build
    # @pytest.mark.severity(pytest.allure.severity_level.NORMAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_correct_login(self):
        url = "http://localhost:3001/login"
        body = {"type":"LOGIN","username":"bm","password":"123456"}
        x = requests.post(url, data=body)
        assert x.status_code == 401
        assert x.elapsed.total_seconds() < 5

    # @pytest.mark.sanity
    # @pytest.mark.severity(pytest.allure.severity_level.NORMAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_incorrect_login_NameNULL(self):
        url = "http://localhost:3001/login"
        body = {"type":"LOGIN","username":"","password":"123456"}
        x = requests.post(url, data=body)
        assert x.status_code == 400
        assert x.elapsed.total_seconds() < 5

    # @pytest.mark.sanity
    # @pytest.mark.severity(pytest.allure.severity_level.NORMAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_incorrect_login_PassNULL(self):
        url = "http://localhost:3001/login"
        body = {"type":"LOGIN","username":"bm","password":""}
        x = requests.post(url, data=body)
        assert x.status_code == 400
        assert x.elapsed.total_seconds() < 5

    """error"""

    # @pytest.mark.server_side_testing
    # @pytest.mark.severity(pytest.allure.severity_level.NORMAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_CreateBankAccount_correctly(self):
        url="http://localhost:3001/comments/mEYl_ZSc5Qqe"
        body = {"transactionId":"mEYl_ZSc5Qqe","content":"hello"}
        x = requests.post(url, data=body)
        assert x.status_code == 401
        assert x.elapsed.total_seconds() < 5

    # @pytest.mark.server_side_testing
    # @pytest.mark.severity(pytest.allure.severity_level.NORMAL)
    @allure.description("Validates 'Real World App' invalid signin credentials")
    def test_register_correctly(self):
        url="http://localhost:3001/users"
        body = {"firstName":"bt","lastName":"ml","username":"mB","password":"12345","confirmPassword":"12345"}
        x = requests.post(url, data=body)
        assert x.status_code == 201
        assert x.elapsed.total_seconds() < 5