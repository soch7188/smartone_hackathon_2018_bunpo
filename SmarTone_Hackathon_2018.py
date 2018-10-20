import json
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from rasa_nlu.model import Interpreter
from scenarios.registration import *

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
    print("request.values.From: ", request.values['From'])
    print("request.values.To: ", request.values['To'])
    print("request.values.Body: ", request.values['Body'])

    user = request.values['From']
    message = request.values['Body']
    parsed_message = interpreter.parse(request.values['Body'])
    print(parsed_message.values())
    for key in parsed_message.keys():
        for value in parsed_message[key]:
            print(key, value)

    initial_text_check(message, parsed_message)

    # Add a message
    resp.message("Hi Minkyung.")

    return str(resp)


@app.route('/get_message', endpoint='get_message', methods=['GET'])
def get_message():
    content = request.get_json()
    print(content)
    return content


if __name__ == '__main__':
    app.run(port=5001)
