## intent:express_cold
- i'm cold
- i feel cold
- why is it so cold here
- can you lower the aircon
- can you make it warmer
- can you adjust the ac

## intent:express_hot
- it's so hot
- i feel hot
- why is it so hot here
- can you make it cooler
- can you adjust the ac

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