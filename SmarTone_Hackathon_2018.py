import json
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from rasa_nlu.model import Interpreter

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from rasa_core.agent import Agent

interpreter = Interpreter.load("./models/current/nlu")
# interpreter = Interpreter.load('./models/current/nlu')

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC976573d88542155f2f8f4b1b5c624da6'
auth_token = '4cbda18e05bce73ab36e5cc280dbff1b'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hey there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+85262232647'
                          )
print(message.sid)

app = Flask(__name__)


# interpreter = Interpreter.load('./models/current/nlu')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/message_in", methods=['GET', 'POST'])
def message_in():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    print("request.values.From: ", request.values['From'])
    print("request.values.To: ", request.values['To'])
    print("request.values.Body: ", request.values['Body'])

    # Add a message
    resp.message("Hi Minkyung.")

    return str(resp)


# @app.route('/get_message', endpoint='get_message', methods=['GET'])
# def get_message():
#     content = request.get_json()
#     print(content)
#     return content


if __name__ == '__main__':
    app.run()

# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from __future__ import unicode_literals

# # from rasa_core.channels.twilio import TwilioInput
# # from rasa_core.agent import Agent
# from rasa_nlu.model import Interpreter
# # from rasa_core.policies.keras_policy import KerasPolicy
# # from rasa_core.policies.memoization import MemoizationPolicy
# # from rasa_core.policies.fallback import FallbackPolicy
# # from rasa_core.interpreter import RasaNLUInterpreter

# interpreter = RasaNLUInterpreter('models/cur/current/nlu',)

# fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
#                           core_threshold=0.3,
#                           nlu_threshold=0.3)

# # load your trained agent
# agent = Agent.load('models/cur/current/dialogue', interpreter=interpreter, policies = [MemoizationPolicy(), KerasPolicy(), fallback])

# # Your Account Sid and Auth Token from twilio.com/console
# account_sid = 'AC976573d88542155f2f8f4b1b5c624da6'
# auth_token = '4cbda18e05bce73ab36e5cc280dbff1b'
# client = Client(account_sid, auth_token)

# input_channel = TwilioInput(
#         # you get this from your twilio account
#         account_sid="YOUR_ACCOUNT_SID",
#         # also from your twilio account
#         auth_token="YOUR_AUTH_TOKEN",
#         # a number associated with your twilio account
#         twilio_number="YOUR_TWILIO_NUMBER"
# )

# # set serve_forever=False if you want to keep the server running
# s = agent.handle_channels([input_channel], 5004, serve_forever=False)
