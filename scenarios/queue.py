import requests
import json

def handle_ask_queue(user, brand):
    # Check if user has access
    res = requests.get(url='http://localhost:5000/api/v1/access/get_access?phone_number=' + user)
    has_access = res.text

    if has_access:
        # Get queue data and respond
        res = requests.get(url='http://localhost:5000/api/v1/queue/get_queue?brand=' + brand)
        crowdedness = res.text

        if str(crowdedness) == "null":
            crowdedness = 0
            return str("The crowdedness of " + str(brand) + " is " + str(crowdedness))

        return str("The crowdedness of " + str(brand) + " is " + str(crowdedness))

    else:
        return "You don't have rights to access the queue data currently. " \
               "Please contribute to the data to get privileged access to our queue data services."


def handle_answer_queue(user, brand, crowdedness):
    requests.post("http://localhost:5000/api/v1/queue/update_queue", json={"phone_number": user, "crowdedness": crowdedness})

    return "Thank you! You now have privileged access to our queue data services"
