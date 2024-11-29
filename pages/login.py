import time
from selenium.webdriver.common.by import By

from config import XPATHs
from library import common


class LoginPage:
    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url

    def login(self):
        driver = common.launch_browser("chrome")
        common.open_url(driver, self.url)
        driver.maximize_window()

        username_input = common.wait_till_element_visible(driver, XPATHs.login_username_xpath)
        username_input.send_keys(self.username)
        password_input = common.wait_till_element_visible(driver, XPATHs.login_password_xpath)
        password_input.send_keys(self.password)
        driver.find_element(By.XPATH, XPATHs.submit_button_xpath).click()
        time.sleep(5)

        assert "Dashboard" in driver.page_source, "Login failed"

        print("Testing -- To be removed")

        return driver
