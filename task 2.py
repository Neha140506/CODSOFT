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
        return "Error: Division by zero is not allowed."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    if choice == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is {result}")

if __name__ == "__main__":
    main()
