Feature: AEG B2B Navigation Menus

  Background:
    Given I navigate to the AEG B2B pre-login page
    When I accept cookies if shown
    And I go to the login form
    And I enter username from Excel
    And I click continue
    And I enter password from Excel
    And I submit the login form
    Then I should be logged in
    And I am on the home page

  @navigation @sales
  Scenario: Sales and Marketing menu shows submenus
    When I click on Sales and Marketing
    Then the Sales and Marketing submenu should be visible

  @navigation @orders
  Scenario: Orders menu shows submenus
    When I click on Orders
    Then the Orders submenu should be visible

  @navigation @training
  Scenario: Training menu shows submenus
    When I click on Training
    Then the Training submenu should be visible

  @navigation @tools
  Scenario: Tools and Services menu shows submenus
    When I click on Tools and Services
    Then the Tools and Services submenu should be visible

  @navigation @footer
  Scenario: First footer heading navigates correctly
    When I scroll to the footer
    And I click on the first footer heading link
    Then the URL should contain sales-and-marketing

  @navigation @footer
  Scenario: Third footer consumer link navigates correctly
    When I scroll to the footer
    And I click on the third footer consumer link
    Then the URL should contain consumer-links
