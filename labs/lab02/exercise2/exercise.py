# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    cost = ((participants / tent_capacity) * tent_price) + meal_price
    return cost

result = calculate_event_cost(230, 4, 50, 20)
print(f"Testing Camping Logistics: {result}")
