out_file = open("out_file.txt", "w")

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 1.0
day = 0
price = INITIAL_PRICE
print("Starting price:${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:

    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)

    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    day += 1
    print(f"On day {day} price is ${price:,.2f} ")
    print(f"On day {day} price is ${price:,.2f} ", file=out_file)

out_file.close()
