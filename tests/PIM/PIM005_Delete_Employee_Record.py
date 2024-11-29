from config.variables import url, username, password
from library.logger import log_event
from pages.login import LoginPage
from pages.pim import PIMTab


logger = log_event()

logger.info(msg="Starting TC PIM005_Delete_Employee")
login_page = LoginPage(url, username, password)
driver = login_page.login()

pim_tab = PIMTab(driver)
pim_tab.click_pim()
pim_tab.search_employee()
pim_tab.delete_employee()
