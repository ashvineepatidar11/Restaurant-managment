menu = {"pizza":20,
        "pasta":15,
        "coffee":10,
        "sandwich":15,
        "burger":15
        }
print("Welcome to python restaurant")
print("Here is our menu\n")

for item,price in menu.items():
 print(f"{item} : ${price}")

order_list = []
while True:
    item = input("Enter item name to order (or type 'done' to finish): ")

    if item.lower() == "done":
        break

    if item in menu:
        order_list.append(item)
        print("Item added to your order")
    else:
        print("Item not found. Please choose from the menu.")

print("\nBill Receipt")

total = 0
for item in order_list:
            price = menu[item]
            total= total + price
            print(f"{item} - ${price}")

print(f"Total Amount: ${total}")
print("Thank you for visiting Python Restaurant!")
