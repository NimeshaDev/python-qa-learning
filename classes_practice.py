class WebPage:
    def __init__(self, url, title):
        self.url=url
        self.title=title

    def Get_Info(self):
        return "page url :"+self.url + "page Title: " + self.title

    def is_login(self):
        if "Login " in self.url:
            return "Yes this is a login page"
        else:
            return "Yes this is not a login page"

login_page= WebPage("saucedemo.com/login","Login ")
home_page= WebPage("saucedemo.com/home","Home ")

print(login_page.Get_Info())
print(home_page.Get_Info())
print(login_page.is_login())
print(home_page.is_login())