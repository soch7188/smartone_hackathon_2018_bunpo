import requests
import json

def register_if_not_already(user):
    print("register_if_not_already is called")
    print("register user: ", user)
    requests.post(url="http://localhost:5000/api/v1/user/register", json={'phone_number': user})
    return "ok"


def update_name(user, entity_1_value):
    requests.post(url="http://localhost:5000/api/v1/user/update_name", json={'phone_number':user, 'name': entity_1_value})
    return str("Hey " + entity_1_value + " how can I help you?")


def handle_greeting(user):
    user = requests.get(url='http://localhost:5000/api/v1/user/get_user?phone_number=' + str(user))
    # return str(user)
    user = json.loads(user.text)
    if user["user"] == None:
        return "Hey, What is your name?"

    if user["user"]["name"]:
        return str("Hey " + user["user"]["name"] + ", how can I help you?")

def handle_ask_user_points(user):
    res = requests.get(url='http://localhost:5000/api/v1/user/points?phone_number=' + str(user))
    points = json.loads(res.text)
    if points == None:
        return "You do not have any points right now."
    return str("You have " + str(points["points"]) + " points.")
