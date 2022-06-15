Feature: Test login and documentation access for equinox admin
  Scenario: Equinox admin consults documentation
    Given I am on Equinox Admin
    When I click on the Documentation Pages link
    Then I am on the Documentation page