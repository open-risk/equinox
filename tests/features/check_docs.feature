Feature: Test login and documentation access for equinox admin
  Scenario: Equinox admin consults documentation
    Given I am on the Equinox Admin Page
    When I click on the Documentation Pages link
    Then I am on the Documentation page