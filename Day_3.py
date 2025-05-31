# Fruit stock and prices
fruits = {
    "Apple": {"stock": 30, "price": 10},
    "Banana": {"stock": 50, "price": 5},
    "Mango": {"stock": 0, "price": 20},
    "Orange": {"stock": 40, "price": 8},
    "Grapes": {"stock": 25, "price": 15}
}

print("Welcome to the Fruit Stall!")
print("Available fruits and prices (per unit):")
for fruit, info in fruits.items():
    print(f"{fruit}: ₹{info['price']} (Stock: {info['stock']})")

# Ask how many different fruits the customer wants
num_items = int(input("\n How many different fruits do you want to buy? "))

cart = {}
total = 0

# Get user input
for _ in range(num_items):
    fruit = input("Enter fruit name: ").capitalize()
    
    if fruit not in fruits:
        print(f"We don't sell {fruit}.")
        continue

    quantity = int(input(f"Enter quantity of {fruit}: "))

    if fruits[fruit]["stock"] == 0:
        print(f"Sorry, {fruit} is out of stock. It will be available tomorrow.")
    elif fruits[fruit]["stock"] < quantity:
        print(f"Only {fruits[fruit]['stock']} {fruit}s are available. Adding all to your cart.")
        cart[fruit] = fruits[fruit]["stock"]
        total += fruits[fruit]["stock"] * fruits[fruit]["price"]
        fruits[fruit]["stock"] = 0
    else:
        cart[fruit] = quantity
        total += quantity * fruits[fruit]["price"]
        fruits[fruit]["stock"] -= quantity

# Show final bill
print("\n Your Cart:")
for fruit, qty in cart.items():
    price = fruits[fruit]["price"]
    print(f"{fruit} x {qty} = ₹{qty * price}")

print(f"\n Total Amount: ₹{total}")
print("Thank you for shopping with us!")
