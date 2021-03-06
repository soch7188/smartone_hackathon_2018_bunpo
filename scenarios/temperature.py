import requests

def handle_express_cold(user):
    requests.post("http://localhost:5000/api/v1/temperature/create_temperature_feeling", json=[{"feeling": "cold"}])

    res = requests.get(url='http://localhost:5000/api/v1/temperature/temperature_concensus_cold')
    print(len(res))

    return "We will try to weaken the air conditioning soon! There are " + len(res) + " number of people who feel cold as well."


def handle_express_hot(user):
    requests.post("http://localhost:5000/api/v1/temperature/create_temperature_feeling", json=[{"feeling": "hot"}])

    res = requests.get(url='http://localhost:5000/api/v1/temperature/temperature_concensus_hot')
    print(len(res))

    return "We will try to strengthen the air conditioning soon! There are " + len(res) + " number of people who feel hot as well."
