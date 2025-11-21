from playwright.sync_api import Page
from pages.login_page_locators import MainPageLocators


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.main_page_locators = MainPageLocators(page)

    def login(self):
        self.page.goto("https://dev.topklik.online/", timeout=60000)
        self.main_page_locators.user_login.fill("tester@inzhenerka.tech")
        self.main_page_locators.user_login.fill("LetsTest!")
        self.main_page_locators.enter.click()
