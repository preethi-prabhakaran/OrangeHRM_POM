from config.variables import url, username, password
from library.logger import log_event
from pages.login import LoginPage
from pages.recruitment import RecruitmentTab

logger = log_event()

logger.info(msg="Starting TC REC002_Add_Candidate")
login_page = LoginPage(url, username, password)
driver = login_page.login()

logger.info(msg="Logged into OrangeHRM application")

recruitment_page = RecruitmentTab(driver)
recruitment_page.click_recruitment()
logger.info(msg="Clicked on Recruitment Tab")

recruitment_page.add_candidate()
logger.info(msg="Candidate added successfully")
