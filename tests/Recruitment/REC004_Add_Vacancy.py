import time

from config.variables import url, username, password
from library.logger import log_event
from pages.login import LoginPage
from pages.recruitment import RecruitmentTab


logger = log_event()
logger.info(msg="Starting TC REC004_Add_Vacancy")

login_page = LoginPage(url, username, password)
driver = login_page.login()

time.sleep(5)
logger.info(msg="Logged into OrangeHRM application")

recruitment_page = RecruitmentTab(driver)
logger.debug("Click Recruitment Tab")
recruitment_page.click_recruitment()
logger.info("Clicked Recruitment Tab")

logger.debug("Starting to add vacancy")
recruitment_page.add_vacancy()
logger.info("Vacancy added")
