from src.driver.interactions import *


class SignInPage:
    @staticmethod
    def clickSignInLink():
        getElement("//div[contains(@class,'HeaderMenu')]//a[contains(.,'Sign in')]").click()

    @staticmethod
    def clickSignInButton():
        getElement("//input[@type='submit']").click()

    @staticmethod
    def setUserName(username):
        typeEditor("//input[contains(@class,'login')]", username)

    @staticmethod
    def setPassword(password):
        typeEditor("//input[contains(@class,'password')]", password)

    @staticmethod
    def signIn(username, password):
        SignInPage.clickSignInLink()
        SignInPage.setUserName(username)
        SignInPage.setPassword(password)
        SignInPage.clickSignInButton()
