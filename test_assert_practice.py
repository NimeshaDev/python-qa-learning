def test_page_title():
    actual_title = "titel 1"
    Expected_title = "titel 1"
    assert actual_title == Expected_title, "Title does not match!"

def test_url_is_correct():
    actual_url = "https://www.google.com"
    Expected_url = "https://www.google.com"
    assert actual_url == Expected_url, "URL does not match!"

def test_item_count():
    item_on_count = 6
    assert item_on_count == 6, "Item count does not match!"
    assert item_on_count > 0, "Page has no items"

def test_username_not_empty():
    username = "standard_user"
    assert len(username) >0, "Username cant be empty!"
    assert username != "", "Username cant be empty!"

