import requests


class CheckoutPage:
    def __init__(self, url, item_count):
        self.url = url
        self.item_count = item_count

    def get_total_items(self):
        return self.item_count

    def can_checkout(self):
        if self.item_count > 0:
            return "Ready to checkout"
        else:
            return "Cart is empty"

def test_can_checkout():
    checkout= CheckoutPage("https://carteira.com.br/checkout", 3)
    assert checkout.can_checkout() == "Ready to checkout"

def test_empty_cart_cannot_checkout():
    checkout = CheckoutPage("https://carteira.com.br/checkout", 0)
    assert checkout.can_checkout() == "Cart is empty"

def test_item_count():
    checkout = CheckoutPage("https://carteira.com.br/checkout", 5)
    assert checkout.get_total_items() == 5

def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200