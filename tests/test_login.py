import pytest
from src.driver.assertion import *
from tests.page.SignInPage import *


@pytest.fixture(autouse=True)
def _driver():
    driver = start()
    yield driver
    driver.quit()


def testCannotLoginAsTest(_driver):
    _driver.get("https://www.github.com")

    SignInPage.signIn("test", "test")

    assertElementPresent("//div[contains(@role,'alert')][normalize-space(text())='Incorrect username or password.']")
