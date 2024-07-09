def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero."

def main():
    print("Welcome to the Basic Calculator!")

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        operation = input("Enter the operation: ")
        
        if operation == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == '+' or operation == '1':
            result = add(num1, num2)
        elif operation == '-' or operation == '2':
            result = subtract(num1, num2)
        elif operation == '*' or operation == '3':
            result = multiply(num1, num2)
        elif operation == '/' or operation == '4':
            result = divide(num1, num2)
        else:
            result = "Error: Invalid operation."
        
        print("The result is:", result)

if __name__ == "__main__":
    main()
