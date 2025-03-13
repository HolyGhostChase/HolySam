# Simple Calculator

# Function to perform calculations
def calculate():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid choice! Please select a valid option.")

# Call the function
calculate()
