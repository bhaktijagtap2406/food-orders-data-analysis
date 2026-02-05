# Food Orders Data Analysis - Core Python
# Author: Bhakti Jagtap

import json

def clean_data(data):
    cleaned_orders = []
    seen_order_ids = set()

    for order in data:
        # 1. Remove duplicate order_id
        if order["order_id"] in seen_order_ids:
            continue
        seen_order_ids.add(order["order_id"])

        # 2. Fix restaurant name (remove extra spaces)
        order["restaurant"] = order["restaurant"].strip()

        # 3. Standardize payment mode
        order["payment_mode"] = order["payment_mode"].upper()

        # 4. Fix price datatype
        if isinstance(order["price"], str):
            order["price"] = int(order["price"])

        # 5. Remove invalid quantity
        if order["quantity"] <= 0:
            continue

        cleaned_orders.append(order)

    return cleaned_orders


# Load data
with open("food_orders.json", "r") as file:
    data = json.load(file)

# Clean data
cleaned_data = clean_data(data)

# Save cleaned data
with open("cleaned_food_orders.json", "w") as file:
    json.dump(cleaned_data, file, indent=4)

print("Data cleaned successfully!")


import json

#Load the json file
def load_data(filename):
    with open(filename,"r") as file:
        data = json.load(file)
    return data
    
#Total revenue
for order in cleaned_data:
    order["revenue"] = order["price"]*order["quantity"]
total_revenue = sum(o["revenue"] for o in cleaned_data)
total_orders = len(cleaned_data)
avg_order_value = total_revenue/total_orders

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)

#Restaurant-wise Revenue

restaurant_revenue = {}

for order in cleaned_data:
    restaurant_revenue[order["restaurant"]] = \
        restaurant_revenue.get(order["restaurant"], 0) + order["revenue"]

print(restaurant_revenue)

#Most Ordered Item
item_count = {}

for o in cleaned_data:
    item_count[o["item"]] = \
        item_count.get(o["item"], 0) + o["quantity"]

print("Most ordered item:", max(item_count, key=item_count.get))


#Sales by City

sales_by_city = {}

for order in data:
    city = order["customer_city"]
    amount = order["price"] * order["quantity"]

    if city in sales_by_city:
        sales_by_city[city] += amount
    else:
        sales_by_city[city] = amount

print("Sales by City:")
for city, sales in sales_by_city.items():
    print(city, ":", sales)


#Most Used Payment Mode

payment_count = {}

for order in data:
    mode = order["payment_mode"]

    if mode in payment_count:
        payment_count[mode] += 1
    else:
        payment_count[mode] = 1

most_used_payment = max(payment_count, key=payment_count.get)

print("Most Used Payment Mode:", most_used_payment)

#Average Delivery Time
total_time = 0

for order in data:
    total_time += order["delivery_time_min"]

average_delivery_time = total_time / len(data)

print("Average Delivery Time:", round(average_delivery_time, 2), "minutes")

