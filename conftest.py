import pytest
class LoginPage():
    def __init__(self):
        self.url = "https://saucedemo.com"
        self.username = "standard_user"
        self.password = "secret_sauce"

    def check_login(self, username, password):
        if username == self.username and password == self.password:
            return "Logged in successfully"
        else:
            return "Login failed"

    def get_url(self):
        return self.url

@pytest.fixture
def login_page():
    page = LoginPage()
    return page

