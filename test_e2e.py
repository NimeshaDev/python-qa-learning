from playwright.sync_api import sync_playwright, expect


def test_complete_shopping_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")
        print("Step 1 — Opened saucedemo")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        print("Step 2 — Logged in")

        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        print("Step 3 — Products page loaded")

        page.locator("button.btn_inventory").first.click()
        print("Step 4 — Product added to cart ")

        cart_count=page.locator(".shopping_cart_badge").text_content()
        assert cart_count == "1", "Cart should have 1 item"
        print ("Step 5 — Cart shows 1 item")

        page.locator(".shopping_cart_link").click()
        expect(page).to_have_url("https://www.saucedemo.com/cart.html")
        print("Step 6 — Cart page opened")

        cart_items=page.locator(".cart_item").count()
        assert cart_items == 1, "Cart should have 1 item"
        print("Step 7 — Item verified in cart")

        browser.close()
        print("Test complete")