# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):

    cost = km_per_liter * price_per_liter * one_way_km
    if cost <= budget:
        return " Money is enough."
    else:
        return "Money does not enough."
    

result = is_budget_sufficient(90, 12, 2, 6700)
print(f"Testing Road Trip Budgeter: {result}")
