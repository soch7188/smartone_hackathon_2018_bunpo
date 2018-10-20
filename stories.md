## ask name greet
* greet OR goodevening OR goodevening OR whatsup
  - utter_just
    - utter_ask_name
    * name
      - action_name_hello

## say goodbye
* goodbye OR goodnight
  - utter_goodbye
    - utter_last

## thankyou
* thankyou
  - utter_thankyou

## express cold
* express_cold
  - utter_answer_cold
    - utter_did_that_help
    * thankyou
      - utter_thankyou

## express cold
* express_hot
  - utter_answer_hot
    - utter_did_that_help
    * mood_affirm
      - utter_thankyou

## express_hungry
* express_hungry
  - utter_what_eat
    - utter_wait_okay
    * mood_affirm
      - utter_top_restaurants
      * thankyou
        - utter_goodbye
          - utter_last
    * mood_deny
      - utter_no_wait_restaurants
      * thankyou
        - utter_goodbye
          - utter_last

