
from Web.FrameWork.Pages.SignupPage import SignupPage
from Web.FrameWork.Pages.SigninPage import SigninPage


def sign_up(self, fname, lname, uname, password, confirmpass):
    driver = self.driver
    signup = SignupPage(driver)
    signup.enter_fname(fname)
    signup.enter_lname(lname)
    signup.enter_unames(uname)
    signup.enter_passwords(password)
    signup.enter_confirmPass(confirmpass)
    signup.click_signup()


def sign_in(self, uname, password):
    driver = self.driver
    signin = SigninPage(driver)
    signin.enter_uname(uname)
    signin.enter_password(password)
    signin.click_signin()
