from playwright.sync_api import Page

class MainPageLocators:
    def __init__(self, page: Page):
        login = page.locator("//input[@name='login']")
        password = page.locator("//input[@name='pass']")
        enter = page.locator("//button[text()='Войти']")
