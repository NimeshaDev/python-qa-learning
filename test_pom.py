import pytest
from playwright.sync_api import sync_playwright
from pages import LoginPage, InventoryPage, CartPage

@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        pg = browser.new_page()
        yield pg
        browser.close()

def test_login(browser_page):
    login = LoginPage(browser_page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in browser_page.url, "Login failed!"
    print("Login test passed ✓")

def test_add_to_cart(browser_page):
    login = LoginPage(browser_page)
    inventory = InventoryPage(browser_page)

    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory.add_first_item_to_cart()

    assert inventory.get_cart_count() == "1", "Cart count wrong!"
    print("Add to cart test passed ✓")

def test_complete_flow(browser_page):
    login = LoginPage(browser_page)
    inventory = InventoryPage(browser_page)
    cart = CartPage(browser_page)

    login.goto()
    login.login("standard_user", "secret_sauce")
    assert inventory.is_loaded(), "Inventory page not loaded!"

    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1"

    cart.goto()
    assert cart.is_loaded(), "Cart page not loaded!"
    assert cart.get_item_count() == 1, "Cart should have 1 item!"
    print("Complete flow test passed ✓")