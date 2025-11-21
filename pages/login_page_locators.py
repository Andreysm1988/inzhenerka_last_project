from playwright.sync_api import Page

class MainPageLocators:
    def __init__(self, page: Page):
        self.user_login = page.locator("//input[@name='login']")
        self.password = page.locator("//input[@name='pass']")
        self.enter = page.locator("//button[text()='Войти']")
