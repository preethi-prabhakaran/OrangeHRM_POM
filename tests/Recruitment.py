import unittest

from config.variables import url, username, password
from library.log_config import log_config
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentTab

class RecruitmentTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This method runs once at the beginning of the test suite
        cls.logger = log_config(suite_name="Tab_Recruitment")
        cls.logger.info("------------Testsuite Recruitment--------------")

        cls.logger.info("Logging into OrangeHRM")
        login_page = LoginPage(url, username, password)
        cls.driver = login_page.login()

        cls.logger.info("Accessing Tab Recruitment")
        cls.recruitment_page = RecruitmentTab(cls.driver)

    def setUp(self):
        # This method runs before each test
        self.logger.info(f"Starting {self._testMethodName}")

    def test_rec_01_access_recruitment(self):
        self.recruitment_page.click_recruitment()

    def test_rec_02_add_candidate(self):
        self.recruitment_page.add_candidate()

    def test_rec_03_search_candidate(self):
        self.recruitment_page.click_recruitment()
        self.recruitment_page.search_candidate()

    def test_rec_04_add_vacancy(self):
        self.recruitment_page.click_recruitment()
        self.recruitment_page.add_vacancy()

    def tearDown(self):
        # This method runs after the test
        self.logger.info(f"End of {self._testMethodName}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.info(f"End of Test Suite Recruitment")

if __name__ == "__main__":
    unittest.main()