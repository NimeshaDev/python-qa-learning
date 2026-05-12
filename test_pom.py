import pytest
import json
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def load_test_data():
    with open("test_data.json", "r") as file:
        return json.load(file)


@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        pg = browser.new_page()
        yield pg
        browser.close()


@pytest.fixture
def test_data():
    return load_test_data()


def test_login(browser_page, test_data):
    login = LoginPage(browser_page)
    login.goto()
    login.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )
    assert "inventory" in browser_page.url, "Login failed!"
    print("Login test passed ✓")


def test_invalid_login(browser_page, test_data):
    login = LoginPage(browser_page)
    login.goto()
    login.login(
        test_data["invalid_user"]["username"],
        test_data["invalid_user"]["password"]
    )
    assert "inventory" not in browser_page.url, "Should not login!"
    print("Invalid login test passed ✓")


def test_locked_user_login(browser_page, test_data):
    login = LoginPage(browser_page)
    login.goto()
    login.login(
        test_data["locked_user"]["username"],
        test_data["locked_user"]["password"]
    )
    assert "inventory" not in browser_page.url, "Locked user should not login!"
    print("Locked user test passed ✓")


def test_add_to_cart(browser_page, test_data):
    login = LoginPage(browser_page)
    inventory = InventoryPage(browser_page)

    login.goto()
    login.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1", "Cart count wrong!"
    print("Add to cart test passed ✓")


def test_complete_flow(browser_page, test_data):
    login = LoginPage(browser_page)
    inventory = InventoryPage(browser_page)
    cart = CartPage(browser_page)

    login.goto()
    login.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )
    assert inventory.is_loaded(), "Inventory page not loaded!"

    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1"

    cart.goto()
    assert cart.is_loaded(), "Cart page not loaded!"
    assert cart.get_item_count() == 1, "Cart should have 1 item!"
    print("Complete flow test passed ✓")