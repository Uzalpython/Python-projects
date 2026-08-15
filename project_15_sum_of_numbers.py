print("===== SUM OF NUMBERS PROGRAM =====")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

total = 0

for number in range(start, end + 1):
    total = total + number

print("The sum of the numbers is:", total)