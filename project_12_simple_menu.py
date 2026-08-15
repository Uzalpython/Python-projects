print("===== SIMPLE MENU =====")
print("1. Say Hello")
print("2. Say Goodbye")
print("3. Show My Name")
print("4. Exit")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Hello! Welcome.")
elif choice == "2":
    print("Goodbye! Have a nice day.")
elif choice == "3":
    name = input("Enter your name: ")
    print("Your name is", name)
elif choice == "4":
    print("Thank you for using the program.")
else:
    print("Invalid choice.")