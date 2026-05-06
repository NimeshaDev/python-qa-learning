
def test_valid_login(login_page):
    results = login_page.check_login("standard_user", "secret_sauce")
    assert results == "Logged in successfully"

def test_invalid_login(login_page):
    results = login_page.check_login("wrong_user", "wrong_pass")
    assert results == "Login failed"

def test_url_is_correct(login_page):
    url = login_page.get_url()
    assert url == "https://saucedemo.com"

def test_empty_credentials(login_page):
    result = login_page.check_login("", "")
    assert result == "Login failed", "Empty credentials should fail!"
