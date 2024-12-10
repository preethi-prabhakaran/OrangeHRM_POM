from datetime import datetime
import time

from selenium.webdriver.common.by import By

from config import variables, XPATHs
from library import common


class BuzzPage:
    def __init__(self, driver):
        self.driver = driver

    def click_buzz(self):
        self.driver.find_element(By.LINK_TEXT, "Buzz").click()
        try:
            page_visible = common.wait_till_element_visible(self.driver, XPATHs.buzz_newsfeed_xpath)
        except Exception as e:
            print("Buzz page is not loaded due to: ", e)
        assert "Buzz" in self.driver.page_source, "Buzz not clicked"

    def post_on_buzz(self):
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys(variables.buzz_post_msg)
        self.driver.find_element(By.XPATH, XPATHs.submit_button_xpath).click()
        current_time = datetime.now()

        # Validate the post
        time.sleep(3)
        formatted_time = current_time.strftime("%Y-%d-%m %I:%M %p")

        assert formatted_time in self.driver.find_element(By.XPATH, XPATHs.buzz_first_post_date).text
        assert variables.buzz_post_msg in self.driver.find_element(By.XPATH, XPATHs.buzz_post_content).text

