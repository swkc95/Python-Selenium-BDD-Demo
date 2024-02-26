@admin
Feature: Admin adding and removing new rooms

  @fixture.browser
  Scenario Outline: Admin creates a room with one additional feature
    Given Admin logs in
    And Admin enters the rooms page
    When Admin provides a valid room info with type of <room_type>
    And Admin adds a room feature - <feature>
    And Admin sends a new room form
    Then Admin sees the new room on the rooms list
    And [API] New room is present in the database
    Examples:
    | room_type | feature  |
    | Single    | WiFi     |
    | Single    | Radio    |

  @fixture.browser
  Scenario: Admin deletes a room
    Given [API] New random room added
    And Admin logs in
    And Admin enters the rooms page
    When Admin finds newly added room and deletes it
    Then Admin does not see the new room on the rooms list
    And [API] Deleted room is not present in the database
