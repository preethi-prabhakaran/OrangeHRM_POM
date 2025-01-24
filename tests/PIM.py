import unittest

from selenium.webdriver.common.by import By
from config import XPATHs, variables
from config.variables import url, username, password
from library.log_config import log_config
from pages.login_page import LoginPage
from pages.pim_page import PIMTab


class PIMTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This method runs once at the beginning of the test suite
        cls.logger = log_config(suite_name="Tab_PIM")
        cls.logger.info("------------Testsuite PIM--------------")

        cls.logger.info("Logging into OrangeHRM")
        login_page = LoginPage(url, username, password)
        cls.driver = login_page.login()

        cls.logger.info("Accessing Tab PIM")
        cls.pim_page = PIMTab(cls.driver)

    def setUp(self):
        # This method runs before each test
        self.logger.info(f"Starting {self._testMethodName}")

    def test_pim_01_access_pim(self):
        self.pim_page.click_pim()

    def test_pim_02_add_new_employee(self):
        self.pim_page.add_employee()

        # Validate that employee is added successfully
        self.assertEqual(variables.empFullName, self.driver.find_element(By.XPATH, XPATHs.employee_details_name_xpath).text)

    def test_pim_03_search_existing_employee(self):
        self.pim_page.click_pim()
        self.pim_page.search_employee()

        # validation
        print(self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text)
        self.assertEqual("(1) Record Found", self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text, "Employee not found")


    def test_pim_04_edit_employee_info(self):
        self.pim_page.click_pim()
        self.pim_page.search_employee()
        self.pim_page.edit_employee_info()

        # Validate that edited info is displayed
        self.assertEqual(variables.empMiddleName, self.driver.find_element(By.NAME, "middleName").get_attribute("value"))

    def test_pim_05_delete_employee(self):
        self.pim_page.click_pim()
        self.pim_page.search_employee()
        self.pim_page.delete_employee()

        # Validate
        self.assertEqual("No Records Found", self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text)

    def tearDown(self):
        # This method runs after the test
        self.logger.info(f"End of {self._testMethodName}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.info(f"End of Test Suite PIM")

if __name__ == "__main__":
    unittest.main()
