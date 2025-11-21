from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_login = page.locator("//input[@name='login']")
        self.password = page.locator("//input[@name='pass']")
        self.enter = page.locator("//button[text()='Войти']")

    def login(self):
        self.page.goto("https://dev.topklik.online/")
        self.user_login.fill("tester@inzhenerka.tech")
        self.password.fill("LetsTest!")
        self.enter.click()
