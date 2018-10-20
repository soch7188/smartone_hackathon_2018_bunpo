import requests


def handle_ask_price(user, brand):
    # Check if user has access
    res = requests.get(url='http://localhost:5000/api/v1/access/get_access?phone_number=' + user)
    has_access = res['item_access']

    if has_access:
        res = requests.get(url='http://localhost:5000/api/v1/item/getItemPrice?brand=' + brand)
        price = res['price']
        print(price)
        return "The price of " + brand + " is " + price
    else:
        return "You don't have rights to access the item price data currently. " \
               "Please contribute to the data to get privileged access to our item price data services."


def handle_answer_price(user, brand, price):
    requests.post("http://localhost:5000/api/v1/item/updateitemprice", json=[{"phone_number": user, "brand": brand, "price": price}])
    return "Thank you! You now have privileged access to our item price data services"
