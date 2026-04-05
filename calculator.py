def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def calculator():
    print("Simple  Calculator")
    print("Operations: Add Subtract Multiply Divide")

    while True:
        
            number1 = float(input("Enter first number: "))
            op = input("Enter operation (Add, Subtract, Multiply, Divide): ")
            number2 = float(input("Enter second number: "))

            if op == "Add":
                result = add(number1, number2)
            elif op == "Subtract":
                result = subtract(number1, number2)
            elif op == "Multiply":
                result = multiply(number1, number2)
            elif op == "Divide":
                result = divide(number1, number2)
            else:
                print("Invalid operation")
                continue

            print("Result:", result)

        


calculator()