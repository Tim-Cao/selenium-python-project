from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.select import Select
from src.driver.browserdriver import *


def acceptAlert():
    WebDriverWait(get_driver(), 5).until(
        expected_conditions.alert_is_present()).accept()


def contextClick(locator):
    actions = ActionBuilder(get_driver())
    actions.pointer_action.context_click(getElement(locator))
    actions.perform()


def doubleClick(locator):
    actions = ActionBuilder(get_driver())
    actions.pointer_action.double_click(getElement(locator))
    actions.perform()


def selectByOption(locator, option):
    Select(getElement(locator)).select_by_value(option)


def scrollBy(position):
    get_driver().execute_script('window.scrollBy(0,' + position + ');')


def typeEditor(locator, value):
    element = getElement(locator)
    element.clear()
    element.send_keys(value)
