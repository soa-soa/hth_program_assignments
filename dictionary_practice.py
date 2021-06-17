# dict_name = {key:value, key:value, key:value}
food_prices = {"chicken":1.59, "beef":1.99, "cheese":1.00, "milk":2.50}

#NBA_players = {"Lebron James": 23, "Kevin Durant": 35, "Stephen Curry": 30, "Damian Lillard": 0}
#Steph_jersey = NBA_players["Stephen Curry"]
#print(NBA_players(Lebron James))

# step 4
chicken = food_prices ["chicken"]
beef = food_prices['beef']
cheese = food_prices['cheese']
milk = food_prices['milk']

print('The price of chicken is', chicken)
print('The price of beef is', beef)
print('The price of cheese is', cheese)
print('The price of milk is', milk)

# step 6 
print('The price of chicken before the price increase is', '$' +str(chicken))

food_prices['chicken'] = 3

chicken = food_prices['chicken']

print('The price of chicken after the price increase is', '$' +str(chicken))


# lab 4 functions practice step 3

def total_price(food_1, food_2):
    total = food_prices[food_1] + food_prices[food_2]
    return total

print(total_price("beef", "cheese"))
print('The total price of beef and cheese is', '$' +str(total_price("beef", "cheese")))

def price_difference(food_1, food_2):
    total = food_prices[food_1] - food_prices[food_2]
    return total

print(total_price("beef", "cheese"))
print('The price difference of beef and cheese is', '$' +str(price_difference("beef", "cheese")))

