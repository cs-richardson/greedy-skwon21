"""
This code finds the least number of coins
needed to give back change to a customer.

San Kwon greedy.py
"""
change = float(input("How much change is owed? "))

while change < 0:
    change = float(input("How much change is owed? "))

# round the given change to two decimal points and convert from dollars to cents
cents = int(100 * round(change, 2))
coins = 0

# calculate the minimum number of coins needed
coins = coins + cents // 25
cents = cents % 25
coins = coins + cents // 10
cents = cents % 10
coins = coins + cents // 5
cents = cents % 5
coins = coins + cents

print("You need " + str(coins) + " coins")
