while True:
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")

    try:
        print(int(x) + int(y))
    except ValueError:
        print("Both inputs must be valid integers. Please try again.")