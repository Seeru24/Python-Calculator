# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main function to run the calculator
def calculator():
    # Print the menu options
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user for the operation
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            # Take input from the user for the two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the operation and print the result
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input")

# Call the main function
calculator() 
