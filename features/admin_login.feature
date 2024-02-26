@admin
Feature: Admin successful and failed log ins

  @fixture.browser
  Scenario: Admin successfully logs in
    Given Admin is on the log in page
    When Admin provides a valid username
    And Admin provides a valid password
    And Admin submits the log in request
    Then Admin is logged in

  @fixture.browser
  Scenario: Admin attempts to log in with an invalid password
    Given Admin is on the log in page
    When Admin provides a valid username
    And Admin provides an invalid password
    And Admin submits the log in request
    Then Admin sees validation markings in the log in form
    And Admin is not logged in
