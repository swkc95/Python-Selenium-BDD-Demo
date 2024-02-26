@customer
Feature: Customer sending messages via contact form

  @fixture.browser
  Scenario: Customer sends a message through the contact form, message is visible for the admin
    Given Customer is on the main page
    And Customer scrolls down to the contact form to send a message
    When Customer provides a valid name in the contact form
    And Customer provides a valid email in the contact form
    And Customer provides a valid phone number in the contact form
    And Customer provides a valid subject in the contact form
    And Customer provides a valid message in the contact form
    And Customer sends a message through the contact form
    Then Admin logs in
    And Admin sees a new message in the mailbox
    And Admin sees the message content

  @fixture.browser
  Scenario: Customer attempts to send a message through the contact form with invalid email
    Given Customer is on the main page
    And Customer scrolls down to the contact form to send a message
    When Customer provides a valid name in the contact form
    And Customer provides an invalid email in the contact form
    And Customer provides a valid phone number in the contact form
    And Customer provides a valid subject in the contact form
    And Customer provides a valid message in the contact form
    And Customer sends a message through the contact form
    Then Customer sees a message about invalid mail formatting
    And [API] New message has not been registered in the database

