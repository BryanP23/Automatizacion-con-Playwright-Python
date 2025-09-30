import pytest
from playwright.sync_api import Page

def test_open_playwright(page):
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()


