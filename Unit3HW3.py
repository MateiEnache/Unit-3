x = input("Enter the first number: ")
y = input("Enter the second number: ")
try:
    print(x+y)
except ValueError:
    print("Both mubers must be integers")