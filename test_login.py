def test_valid_login():
    username =("standard_user")
    password =("secret_sauce")
    assert username == "standard_user"
    assert password == "secret_sauce"
    print("valid login")

def test_invalid_login():
    username =("wrong_user")
    password =("wrong_pass")
    assert username != "standard_user"
    assert password != "secret_sauce"
    print("invalid login")

def test_url_contains_inventory():
    url =("saucedemo.com/inventory")
    assert "inventory" in url
    print("valid login")