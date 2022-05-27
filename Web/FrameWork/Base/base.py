from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Web.FrameWork.Locators.SignupLocators import SignupLocators


import pytest


class Base:

    @pytest.fixture(params=["chrome", "firefox"])
    def init_driver(self, request):
        if request.param == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        if request.param == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver = self.driver
        self.driver.get("http://localhost:3000")
        self.driver.implicitly_wait(10)

        yield
        self.driver.close()
        self.driver.quit()


    @pytest.fixture(params=["chrome", "firefox"])
    def init_driver_signup(self, request):
        if request.param == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        if request.param == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver = self.driver
        self.driver.get("http://localhost:3000/signup")
        self.driver.implicitly_wait(10)

        yield
        self.driver.close()
        self.driver.quit()
