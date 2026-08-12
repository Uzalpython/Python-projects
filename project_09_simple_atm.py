balance = 50000

print("===== SIMPLE ATM =====")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    print("Your balance is ₦", balance)

elif choice == "2":
    amount = float(input("Enter deposit amount: "))
    balance = balance + amount
    print("Deposit successful.")
    print("Your new balance is ₦", balance)

elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful.")
        print("Your new balance is ₦", balance)
    else:
        print("Insufficient balance.")

else:
    print("Invalid choice.")