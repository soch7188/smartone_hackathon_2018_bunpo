
## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## express cold
* express_cold
  - utter_answer_cold
  - utter_did_that_help

## express cold
* express_hot
  - utter_answer_hot
  - utter_did_that_help

## express_hungry
* express_hungry
  - utter_what_eat
  - utter_wait_okay
    * mood_affirm
      - utter_top_restaurants
