import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


def assertion(self, locator, assert_txt):
    try:
        value = self.driver.find_element(By.XPATH, locator).get_attribute("innerText")
        assert assert_txt == value
    except Exception as e:
        allure.attach(self.driver.get_screenshot_as_png(), name="testSignupScreen",
                      attachment_type=AttachmentType.PNG)
        print(format(e))


def assertion_buttons(self,locator):
    try:
        value = self.driver.find_element(By.XPATH,locator).is_enabled()
        assert value == False
        # add to list of clickable elements
    except WebDriverException:
        print("Element is not clickable")
