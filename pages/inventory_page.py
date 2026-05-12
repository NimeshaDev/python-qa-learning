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