class loginPage:
    def __init__(self):
        self.url = "https://saucedemo.com"
        self.title = "Swag Labs"

    def get_url(self):
        return self.url

    def check_title(self, expected):
        if self.title == expected:
            return ("Title check passed")
        else:
            return ("Title check failed")

login= loginPage()
print(login.get_url())
print(login.check_title("Swag Labs"))
print(login.check_title("Wrong Title"))
