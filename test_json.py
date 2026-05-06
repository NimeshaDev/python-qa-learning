import json
import pytest

def load_test_data():
    with open("test_data.json") as file:
        data = json.load(file)
    return data

class LoginPage:
    def __init__(self,url):
        self.url =url

    def check_login(self, username, password):
        if username == "standard_user" and password == "secret_sauce":
            return "Logged in successfully"
        else:
            return "Login Failed"

def test_valid_user_login():
    data = load_test_data()
    page= LoginPage(data["base_url"])
    result= page.check_login(data["valid_user"]["username"],data["valid_user"]["password"])
    assert result == "Logged in successfully", "Valid user should login!"

def test_invalid_user_login():
    data = load_test_data()
    page= LoginPage(data["base_url"])
    result= page.check_login(data["invalid_user"]["username"],data["invalid_user"]["password"])
    assert result == "Login Failed", "Invalid user should fail!"

def test_locked_user_login():
    data = load_test_data()
    page= LoginPage(data["base_url"])
    result= page.check_login(data["locked_user"]["username"],data["locked_user"]["password"])
    assert result == "Login Failed", "Locked user should fail!"

def test_base_url_is_correct():
    data = load_test_data()
    page= LoginPage(data["base_url"])=="https://saucedemo.com", "URL is wrong!"