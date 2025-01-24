import unittest
# import sys
#
# sys.path.append('../')

from config.variables import url, username, password
from library.log_config import log_config
from pages.buzz_page import BuzzPage
from pages.login_page import LoginPage


class BuzzTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method runs once at the beginning of the test suite
        cls.logger = log_config(suite_name = "Tab_Buzz")
        cls.logger.info("------------Testsuite Buzz--------------")

        cls.logger.info("Logging into OrangeHRM")
        login_page = LoginPage(url, username, password)
        cls.driver = login_page.login()

        cls.logger.info("Accessing Tab Buzz")
        cls.buzz_page = BuzzPage(cls.driver)

    def setUp(self):
        # This method runs before each test
        self.logger.info(f"Starting {self._testMethodName}")

    def test_buzz_01_access_buzz(self):
        self.buzz_page.click_buzz()
        self.assertIn("Buzz", self.driver.page_source, "Buzz not clicked")


    def test_buzz_02_post_buzz(self):
        self.buzz_page.post_on_buzz()

    def tearDown(self):
        # This method runs after the test
        self.logger.info(f"End of {self._testMethodName}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.info(f"End of Test Suite Buzz")

if __name__ == "__main__":
    unittest.main()