@customer
Feature: Customer booking a room

  @fixture.browser
  Scenario: Customer successfully books a room
    Given [API] New random room added
    And Customer is on the main page
    And Customer clicks to book the new room
    When Customer provides a valid first name in the booking form
    And Customer provides a valid last name in the booking form
    And Customer provides a valid email in the booking form
    And Customer provides a valid phone number in the booking form
    And Customer provides a valid booking date
    And Customer sends a booking request
    Then Customer sees confirmation message about successful booking
    And [API] New booking is registered in the database

  @fixture.browser
  Scenario: Customer attempts to book a room without passing phone number
    Given [API] New random room added
    And Customer is on the main page
    And Customer clicks to book the new room
    When Customer provides a valid first name in the booking form
    And Customer provides a valid last name in the booking form
    And Customer provides a valid email in the booking form
    And Customer provides a valid booking date
    And Customer sends a booking request
    Then Customer sees validation message about invalid phone number
    And [API] New booking has not been registered in the database
