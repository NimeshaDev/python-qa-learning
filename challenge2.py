class CartPage:
    def __init__(self, url, item_count):
        self.url = url
        self.item_count = item_count

    def get_item_count(self):
        return self.item_count

    def is_cart_empty(self):
        if self.item_count == 0:
            return "Cart is empty"
        else:
            return "Cart has items"

def test_cart_has_items():
    Cart= CartPage("https://carteira.com.br/", 3)
    assert Cart.get_item_count() == 3

def test_empty_cart():
    Cart= CartPage("https://carteira.com.br/", 0)
    assert Cart.is_cart_empty() == 'Cart is empty'