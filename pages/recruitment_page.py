import time
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from config import variables, XPATHs
from library import common


class RecruitmentTab:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_recruitment(self):
        self.driver.find_element(By.LINK_TEXT, "Recruitment").click()
        time.sleep(3)
        assert "Recruitment" in self.driver.find_element(By.TAG_NAME, "h6").text

    def add_candidate(self):
        try:
            self.driver.find_element(By.XPATH, XPATHs.add_button_xpath).click()
            time.sleep(5)
            assert "Add Candidate" in self.driver.find_element(By.XPATH, XPATHs.add_candidate_title_xpath).text

            self.driver.find_element(By.NAME, "firstName").send_keys(variables.firstName)
            self.driver.find_element(By.NAME, "lastName").send_keys(variables.lastName)
            self.driver.find_element(By.XPATH, XPATHs.add_candidate_email_xpath).send_keys(variables.candidate_email)

            self.driver.find_element(By.XPATH, XPATHs.save_button_xpath).click()

            # Wait until the Application Stage / candidate details page appears
            common.wait_till_element_visible(self.driver, XPATHs.candidate_details_xpath)

            # Validate the added name in the page
            assert variables.fullName in self.driver.find_element(By.XPATH, XPATHs.candidate_details_fullname_xpath).text
        except Exception as e:
            print(f"Failed to add candidate due to: {e}")

    def search_candidate(self):
        self.driver.find_element(By.XPATH, XPATHs.search_candidate_xpath).send_keys(variables.firstName)
        time.sleep(3)

        self.driver.find_element(By.XPATH, XPATHs.search_candidate_xpath).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        self.driver.find_element(By.XPATH, XPATHs.search_button_xpath).click()
        time.sleep(5)

        print(self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text)
        # recruitment_log.info(msg=self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text)
        assert "Record Found" in self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text

    def add_vacancy(self):
        self.driver.find_element(By.LINK_TEXT, "Vacancies").click()
        common.wait_till_element_visible(self.driver, XPATHs.h5_xpath)
        self.driver.find_element(By.XPATH, XPATHs.add_button_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, XPATHs.vacancy_name_xpath).send_keys(variables.vacancyName)

        # Click dropdown arrow of Job Title
        self.driver.find_element(By.XPATH, XPATHs.job_title_dropdown_xpath).click()
        options = self.driver.find_elements(By.XPATH, XPATHs.job_title_dropdown_options_xpath)
        time.sleep(3)

        # Select HR Manager from the dropdown
        self.driver.find_element(By.XPATH, XPATHs.hr_manager_dropdown_xpath).click()

        time.sleep(5)

        # Select Hiring Manager
        self.driver.find_element(By.XPATH, XPATHs.hiring_manager_xpath).send_keys(variables.hiringManagerFirstName)
        time.sleep(3)
        self.driver.find_element(By.XPATH, XPATHs.hiring_manager_xpath).send_keys(Keys.ARROW_DOWN, Keys.ENTER)

        self.driver.find_element(By.XPATH, XPATHs.save_button_xpath).click()
        time.sleep(10)
        assert variables.vacancyName in self.driver.find_element(By.XPATH, XPATHs.vacancy_name_xpath).get_attribute("value")


