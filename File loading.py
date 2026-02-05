# Food Orders Data Analysis - Core Python
# Author: Bhakti Jagtap

import json

#Load the json file
def load_data(filename):
    with open(filename,"r") as file:
        data = json.load(file)
    return data

# Display Order
def display_order(data):
    print("Order IDs ")
    for order in data:
        print(f"ID : {order['order_id']} - Date : {order['date']} - Restaurant : {order['restaurant']} - Item : {order['item']} - Price : {order['price']} - Quantity : {order['quantity']} - Payment_mode : {order['payment_mode']}")

#Load and display data
data = load_data("food_orders.json")
display_order(data)

