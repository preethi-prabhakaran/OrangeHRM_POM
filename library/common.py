from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def launch_browser(browser):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
        return driver
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
        return driver
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
        return driver
    else:
        print("Browser not supported")
        raise ValueError


def open_url(driver: webdriver, url):
    driver.get(url)


def wait_till_element_visible(driver: webdriver, element_xpath):
    wait = WebDriverWait(driver, 10)
    element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, element_xpath)))
    return element
