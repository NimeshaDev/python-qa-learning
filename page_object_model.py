from xml.dom.minidom import ProcessingInstruction


class LoginPage:
    def __init__(self):
        self.url = "https://saucedemo.com"
        self.username = "user-name"
        self.password = "password"
        self.login_button = "login"

    def get_url(self):
        return self.url

    def enter_credentials(self,username,password):
        print("Typing Username " + username)
        print("Typing Password " + password)
        print("Click Login Button")

    def verify_login(self, expected_url):
        actual_url = "saucedemo.com/inventory"
        if expected_url in actual_url:
            return "LOGIN SUCCESSFUL"
        else:
            return "LOGIN FAILED"

login =LoginPage()
print(login.get_url())
login.enter_credentials("standard_user", "secret_sauce")
print(login.verify_login("inventory"))
print(login.verify_login("checkout"))