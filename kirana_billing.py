receipt = {}
item = ""
total = 0
print("Welcome to the receipt generator program! Enter \"Total\" to quit the program!\n")
while True:
    item = input("Enter the product's name: ").title()
    if item == "Total":
        break
    price = int(input(f"Enter {item}'s price: "))

    total += price
    receipt.update({item: price})

receipt_keys = list(receipt.keys())
receipt_values = list(receipt.values())

print("\n")
for i in range(len(receipt_keys)):
    print(f"{i+1}. {receipt_keys[i]} -> {receipt_values[i]}")
print(f"\nTotal = {total}")