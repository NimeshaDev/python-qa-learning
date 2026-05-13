from idlelib import browser

import pytest
import json
from pytest_bdd import given, when, then, scenario
from playwright.sync_api import sync_playwright

from classes_practice import login_page
from pages import inventory_page


def load_test_data():
    with open("test_data.json", "r") as file:
        return json.load(file)

@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        pg = browser.new_page()
        yield pg
        browser.close()

@pytest.fixture
def context(browser_page):
    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage
    return {
        "page": browser_page,
        "login": LoginPage(browser_page),
        "inventory": InventoryPage(browser_page),
        "data": load_test_data()
    }

@scenario("features/login.feature", "Valid user can login")
def test_valid_user_login():
    pass

@scenario("features/login.feature", "Invalid user cannot login")
def test_invalid_login():
    pass

@scenario("features/login.feature", "Locked user cannot login")
def test_locked_user():
    pass

@given("I am on the login page")
def go_to_login(context):
    context["login"].goto()

def login_valid(context):
    context["login"].login(
        context["data"]["valid_user"]["username"],
        context["data"]["valid_user"]["password"]
    )

@when("I login with valid credentials")
def login_valid(context):
    context["login"].login(
        context["data"]["valid_user"]["username"],
        context["data"]["valid_user"]["password"]
    )
@when("I login with invalid credentials")
def login_invalid(context):
    context["login"].login(
        context["data"]["invalid_user"]["username"],
        context["data"]["invalid_user"]["password"]
    )


@when("I login with locked user credentials")
def login_locked(context):
    context["login"].login(
        context["data"]["locked_user"]["username"],
        context["data"]["locked_user"]["password"]
    )

@then("I should see the inventory page")
def check_inventory(context):
    assert "inventory" in context["page"].url, "Login failed!"
    print("Inventory page loaded ✓")


@then("I should not see the inventory page")
def check_not_inventory(context):
    assert "inventory" not in context["page"].url, "Should not login!"
    print("Login correctly rejected ✓")
