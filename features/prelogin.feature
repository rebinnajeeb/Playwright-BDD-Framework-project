Feature: AEG B2B Pre-Login Page

  # This smoke scenario works out of the box (no real locators needed) and
  # proves the framework is wired up correctly.
  @smoke
  Scenario: The pre-login page loads successfully
    Given I navigate to the AEG B2B pre-login page
    Then the current url should contain "pre-login"

  # Log in using test credentials from Excel (TestData/LoginData.xlsx)
  # Change the market in ConfigurationData/conf.ini to test different markets
  @login
  Scenario: Log in with credentials from Excel
    Given I navigate to the AEG B2B pre-login page
    When I accept cookies if shown
    And I go to the login form
    And I enter username from Excel
    And I click continue
    And I enter password from Excel
    And I submit the login form
    Then I should be logged in

  @invalidlogin
  Scenario: Login fails with invalid credentials
    Given I navigate to the AEG B2B pre-login page
    When I accept cookies if shown
    And I go to the login form
    And I enter invalid username
    And I click continue
    And I enter invalid password
    And I submit the login form
    Then I should see a login error
