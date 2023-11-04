x = input("Please enter a number: ")
y = input("Please enter a number: ")
operation = input("Choose an operation to perform (*, +, -, /): ")


if operation == "*":
    print(float(x) * float(y))
elif operation == "+":
    print(float(x) + float(y))
elif operation == "-":
    print(float(x) - float(y))
else:
    print(float(x) / float(y))
