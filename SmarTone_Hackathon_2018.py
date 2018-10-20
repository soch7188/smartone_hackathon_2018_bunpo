import json
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from rasa_nlu.model import Interpreter
from scenarios.registration import *
from scenarios.queue import *
from scenarios.temperature import *
from scenarios.item import *

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

interpreter = Interpreter.load('/Users/ziwon/Documents/SmarTone_Hackathon_2018/models/current/nlu')

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC976573d88542155f2f8f4b1b5c624da6'
auth_token = '4cbda18e05bce73ab36e5cc280dbff1b'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+85261318805'
                          )
print(message.sid)

# message = client.messages.create(
#                               body='Hello there!',
#                               from_='whatsapp:+14155238886',
#                               to='whatsapp:+85262232647'
#                           )
# print(message.sid)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/send_message', methods=['POST'])
# def send_message():
#     message = 'hey!'
#     result = interpreter.parse(message)
#     result_ = json.dumps(result, indent=2)
#
#     return jsonify(result_)

@app.route("/message_in", methods=['GET', 'POST'])
def message_in():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Step 1: Extract Intent & Entities
    print("request.values.From: ", request.values['From'])
    print("request.values.To: ", request.values['To'])
    print("request.values.Body: ", request.values['Body'])

    user = request.values['From']
    message = request.values['Body']
    parsed_message = interpreter.parse(request.values['Body'])
    print(parsed_message)

    intent_name = parsed_message['intent']['name']
    intent_conf = parsed_message['intent']['confidence']

    if (parsed_message['entities']):
        entity_1_name = parsed_message['entities'][0]['entity']
        entity_1_value = parsed_message['entities'][0]['value']

        if (parsed_message['entities'][1]):
            entity_2_name = parsed_message['entities'][1]['entity']
            entity_2_value = parsed_message['entities'][1]['value']


    # Step 2: Hanlde Scenarios
    resp.message("Sorry, I cannot understand what you are saying yet, but I will learn soon!")

    # 1) Registration
    register_if_not_already(user)
    # initial_text_check(user, intent_name, entity_1_name, entity_1_value, entity_2_name, entity_2_value)

    # 2) If intent=='greeting' and user has no name, ask for name
    if intent_name=='greet':
        resp.message(handle_greeting)

    if intent_name=='ask_user_points':
        resp.message(handle_ask_user_points)

    # 3)
    if intent_name=='ask_queue':
        resp.message(handle_ask_queue)

    if intent_name == 'answer_queue':
        resp.message(handle_answer_queue)

    if intent_name=='ask_price':
        resp.message(handle_ask_price)

    if intent_name=='answer_price':
        resp.message(handle_answer_price)

    if intent_name=='express_cold':
        resp.message(handle_express_cold)

    if intent_name=='express_hot':
        resp.message(handle_express_hot)

    if intent_name == 'name':
        # Update Name
        if entity_1_value:
            update_name(user, entity_1_value)
        else:
            resp.message("Sorry I didin't get your name.")

    # Add a message
    # resp.message("Hi Minkyung.")

    return str(resp)


@app.route('/get_message', endpoint='get_message', methods=['GET'])
def get_message():
    content = request.get_json()
    print(content)
    return content


if __name__ == '__main__':
    app.run(port=5001)
