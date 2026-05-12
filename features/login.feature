Feature: Login functionality
  As a user
  I want to login to saucedemo
  So that I can access the products

  Scenario: Valid user can login
    Given I am on the login page
    When I login with valid credentials
    Then I should see the inventory page

  Scenario:  Invalid user cannot login
    Given I am on the login page
    When I login with invalid credentials
    Then I should not see the inventory page

  Scenario: Locked user cannot login
    Given I am on the login page
    When I login with locked user credentials
    Then I should not see the inventory page


