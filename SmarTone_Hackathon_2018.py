import json
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from rasa_nlu.model import Interpreter

app = Flask(__name__)
interpreter = Interpreter.load('./models/current/nlu')

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/send_message', methods=['POST'])
def send_message():
	message = 'hey!'
	result = interpreter.parse(message)
	result_ = json.dumps(result, indent=2)

	return jsonify(result_)

@app.route('/get_message', endpoint='get_message', methods=['GET'])
def get_message():
	content = request.get_json()
	print(content)
	return content

if __name__ == '__main__':
    app.run()