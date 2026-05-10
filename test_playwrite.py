from playwright.sync_api import sync_playwright
from urllib3.util import url


def test_open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page= browser.new_page()

        page.goto("https://saucedemo.com")
        print("Browser opened")

        assert page.title() == "Swag Labs", "Title is wrong!"
        print("Title check is correct")

        browser.close()

def test_login():
    with sync_playwright() as p:
        browser =p.chromium.launch(headless=False)
        page= browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.get_by_placeholder("Username").fill("standard_user")
        print("Username name print")

        page.get_by_placeholder("Password").fill("secret_sauce")
        print("Password name print")

        page.get_by_role("button", name="Login").click()
        print("Login button clicked")

        assert "inventory" in page.url, "Login failed — wrong URL"
        print("Login successful")
        print("Current URL: ", page.url)

        browser.close()