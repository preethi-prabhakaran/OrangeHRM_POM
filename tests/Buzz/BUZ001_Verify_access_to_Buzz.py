from config.variables import url, username, password
from library.logger import log_event
from pages.buzz import BuzzPage
from pages.login import LoginPage

logger = log_event()

logger.info(msg="Starting TC BUZ001_Verify_Access_to_Buzz_Tab")
login_page = LoginPage(url, username, password)
driver = login_page.login()

buzz_page = BuzzPage(driver)
buzz_page.click_buzz()

