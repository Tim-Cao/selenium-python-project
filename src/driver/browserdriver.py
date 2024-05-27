import threading
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from src.driver.chromedrivermanager import ChromeDriverManager

_threadLocal = threading.local()


def start():
    _threadLocal.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    _threadLocal.driver.delete_all_cookies()
    _threadLocal.driver.maximize_window()

    return _threadLocal.driver


def get_driver():
    return _threadLocal.driver


def pause(timeout):
    get_driver().implicitly_wait(timeout)

def getElement(locator):
    waitForElementPresent(locator)

    return get_driver().find_element(By.XPATH, locator)

def waitForElementPresent(locator):
    try:
        WebDriverWait(get_driver(), 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator))
        )
    except TimeoutException:
        pass

def waitForElementNotPresent(locator):
    try:
        WebDriverWait(get_driver(), 5).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, locator))
        )
    except TimeoutException:
        pass
