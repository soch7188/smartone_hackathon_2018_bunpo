import requests


def handle_ask_queue(user, floor, brand):
    # Check if user has access
    res = requests.get(url='http://localhost:5000/api/v1/access/get_access?phone_number=' + user)
    has_access = res['queue_access']

    if has_access:
        # Get queue data and respond
        res = requests.get(url='http://localhost:5000/api/v1/queue/get_queue?floor=' + floor+'?brand=' + brand)
        crowdedness = res['crowdedness']
        print(crowdedness)
        return "The crowdedness of " + brand + "at floor " + floor + " is " + crowdedness
    else:
        return "You don't have rights to access the queue data currently. " \
               "Please contribute to the data to get privileged access to our queue data services."


def handle_answer_queue(user, floor, brand, crowdedness):
    requests.post("http://localhost:5000/api/v1/queue/update_queue", json=[{"phone_number": user, "floor": floor, "brand": brand, "crowdedness": crowdedness}])
    return "Thank you! You now have privileged access to our queue data services"
