password = input("Enter your password: ")

if len(password) < 6:
    print("Password is too short.")
elif len(password) < 10:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")