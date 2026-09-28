expenses = []
total = 0
print("--- Welcome to Expense Tracker ---")
print("Type 'done' to finish\n")
while True:
    name = input("Expense Name: ")
    if name.lower() == "done":
        break
    try:
        amount = float(input(f"Amount for {name}: Rs. "))
        expenses.append({"name": name, "amount": amount})
        total += amount
        print(f"Added! Current Total: Rs. {total}\n")
    except ValueError:
        print("Please enter a valid number!\n")
print("\n--- Expense Summary ---")
for item in expenses:
    print(f"{item['name']}: Rs. {item['amount']}")
print(f"\nTotal Expense: Rs. {total}")
