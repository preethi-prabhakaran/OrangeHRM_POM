from config.variables import url, username, password
from library.logger import log_event
from pages.recruitment import RecruitmentTab
from pages.login import LoginPage

logger = log_event()

logger.info(msg="Starting TC REC001_Verify_Access_to_Recruitment_Tab")
login_page = LoginPage(url, username, password)
driver = login_page.login()

recruitment_page = RecruitmentTab(driver)
recruitment_page.click_recruitment()


