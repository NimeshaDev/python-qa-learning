
class ProductPage:
    def __init__(self, url, title):
        self.url = url
        self.title = title

    def get_title(self):
        return self.title

    def has_products(self):
        if "Products" in self.title :
            return "Products found"
        else:
            return "Product not found"

def test_title_is_correct():
        page = ProductPage("saucedemo.com/products", "Products")
        assert page.get_title() == "Products", "Title should be Products!"

def test_products_found():
        page = ProductPage("saucedemo.com/products", "Products")
        result = page.has_products()
        assert result == "Products found", "Should find products!"