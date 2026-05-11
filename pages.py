class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com"

    def goto(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def get_title(self):
        return self.page.title()


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/inventory.html"

    def is_loaded(self):
        return "inventory" in self.page.url

    def add_first_item_to_cart(self):
        self.page.locator(".btn_inventory").first.click()

    def get_cart_count(self):
        return self.page.locator(
            ".shopping_cart_badge").text_content()


class CartPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/cart.html"

    def goto(self):
        self.page.locator(".shopping_cart_link").click()

    def is_loaded(self):
        return "cart" in self.page.url

    def get_item_count(self):
        return self.page.locator(".cart_item").count()