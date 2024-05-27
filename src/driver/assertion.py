from src.driver.browserdriver import *


def assertElementPresent(locator):
    waitForElementPresent(locator)
    assert getElement(locator).is_displayed()

def assertCheck(locator):
    getElement(locator).is_selected()

def assertTextEquals(locator, value):
    assert value == getElement(locator).text

def assertCSSValue(locator, property, value):
    assert value == getElement(locator).value_of_css_property(property)

def assertElementAttribute(locator, attribute, value):
    assert value == getElement(locator).get_property(attribute)
