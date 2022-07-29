total_price = 0
items = int(input("Items:"))
for i in range(items):
    total_price += float(input("Price of item:"))
    if total_price > 100:
        total_price = total_price * 0.9
print(f"Total price for {items} items is {total_price}$")
