Feature: Test login for equinox admin
  Scenario: Equinox admin login
    Given I am an Equinox Admin
    When I click on the Login link
    Then I am on the Equinox Admin page