number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Do you wish to add, subtract, multiply or divide these numbers: ").strip().lower()

if operator in ("add", "Add", "+"):
    answer = number1 + number2
    print("\nNumber 1 + Number 2 =", answer)
elif operator in ("subtract", "Subtract", "-"):
    answer = number1 - number2
    print("\nNumber 1 - Number 2 =", answer)
elif operator in ("multiply", "Multiply", "*"):
    answer = number1 * number2
    print("\nNumber 1 x Number 2 =", answer)
elif operator in ("divide", "Divide", "/"):
    if number2 == 0:
        print("\nError: Division by zero")
    else:
        answer = number1 / number2
        print("\nNumber 1 / Number 2 =", answer)
else:
    print("\nYou have entered an invalid response")