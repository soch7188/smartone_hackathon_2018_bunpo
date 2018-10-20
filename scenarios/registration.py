import requests


def register_if_not_already(user):
    requests.post("http://localhost:5000/api/v1/user/register", json=[{"phone_number": user}])


def update_name(user, entity_1_value):
    requests.post("http://localhost:5000/api/v1/user/update_name", json=[{"phone_number": user, "name": entity_1_value}])


def handle_greeting(user):
    user = requests.get(url='http://localhost:5000/api/v1/user/get_user?phone_number=' + user)
    print("user['name']: ")
    print(user['name'])
    if user['name']:
        return "Hey!"
    else:
        return "Nice to meet you too! What's your name?"


def handle_ask_user_points(user):
    res = requests.get(url='http://localhost:5000/api/v1/user/points?phone_number=' + user)
    points = res['points']
    print(points)
    return "You have " + points + "."
