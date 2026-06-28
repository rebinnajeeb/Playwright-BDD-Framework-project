Feature: AEG B2B Logout

  @logout
  Scenario: User can log out from the partner portal
    Given I navigate to the AEG B2B pre-login page
    When I accept cookies if shown
    And I go to the login form
    And I enter username from Excel
    And I click continue
    And I enter password from Excel
    And I submit the login form
    Then I should be logged in
    Given I am on the home page
    When I open the profile dropdown
    And I click logout
    Then I should be back on the pre-login page
