# add this at the bottom of test_login.py

class LoginPage:
    def __init__(self):
        self.url = "https://saucedemo.com"
        self.username = "standard_user"
        self.password = "secret_sauce"

    def check_login(self, username, password):
        if username == self.username and password == self.password:
            return "Login Successful"
        else:
            return "Login Failed"

    def get_url(self):
        return self.url

def test_valid_user_can_login():
    page = LoginPage()
    result = page.check_login("standard_user", "secret_sauce")
    assert result == "Login Successful", "Valid user should login!"

def test_wrong_password_fails():
    page = LoginPage()
    result = page.check_login("standard_user", "wrong_pass")
    assert result == "Login Failed", "Wrong password should fail!"

def test_empty_username_fails():
    page = LoginPage()
    result = page.check_login("", "secret_sauce")
    assert result == "Login Failed", "Empty username should fail!"