from playwright.sync_api import Page, expect
from pages.login_page import MainPage
import allure


@allure.title("Проверка логина")
def test_login(page: Page):
    main_page = MainPage(page)

    main_page.login()
