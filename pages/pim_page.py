import time
from selenium.webdriver.common.by import By
from config import variables, XPATHs


class PIMTab:
    def __init__(self, driver):
        self.driver = driver

    def click_pim(self):
        self.driver.find_element(By.LINK_TEXT, "PIM").click()
        time.sleep(2)
        assert "PIM" in self.driver.page_source, "PIM not clicked"

    def add_employee(self):
        self.driver.find_element(By.XPATH, XPATHs.add_button_xpath).click()
        time.sleep(5)

        self.driver.find_element(By.NAME, "firstName").send_keys(variables.empFirstName)
        self.driver.find_element(By.NAME, "lastName").send_keys(variables.empLastName)

        # use get_attribute("value") to capture dynamic values from webpage
        emp_id = self.driver.find_element(By.XPATH, XPATHs.employee_id_xpath).get_attribute("value")
        print(emp_id)

        self.driver.find_element(By.XPATH, XPATHs.submit_button_xpath).click()
        time.sleep(10)

    def search_employee(self):
        self.driver.find_element(By.XPATH, XPATHs.emp_name_xpath).send_keys(variables.empFirstName)
        self.driver.find_element(By.XPATH, XPATHs.search_button_xpath).click()
        time.sleep(7)

    def edit_employee_info(self):
        self.driver.find_element(By.XPATH, XPATHs.edit_button_xpath).click()
        time.sleep(5)

        # Edit info
        self.driver.find_element(By.NAME, "middleName").send_keys(variables.empMiddleName)
        self.driver.find_element(By.XPATH, XPATHs.emp_edit_info_save_xpath).click()
        time.sleep(7)


    def delete_employee(self):
        # click on delete button
        self.driver.find_element(By.XPATH, XPATHs.delete_icon_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, XPATHs.delete_confirm_button_xpath).click()
        time.sleep(5)


