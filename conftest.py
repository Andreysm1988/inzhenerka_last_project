import os
import pytest
from playwright.sync_api import sync_playwright

headless_mode = os.getenv("CI") == "true"
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()