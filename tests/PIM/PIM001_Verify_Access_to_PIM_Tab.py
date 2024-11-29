from config.variables import url, username, password
from library.logger import log_event
from pages.login import LoginPage
from pages.pim import PIMTab

logger = log_event()
logger.info(msg="Starting TC PIM001_Verify_Access_to_PIM_Tab")

login_page = LoginPage(url, username, password)
driver = login_page.login()

pim_tab = PIMTab(driver)
pim_tab.click_pim()
