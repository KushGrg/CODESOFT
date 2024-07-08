def calculator():
    print("Welcome to the Simple Calculator!")

    while True:
        print("\nChoose the operation you want to perform:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

       
        operation = input("Enter the number corresponding to the operation (1/2/3/4/5): ")

        
        if operation == '5':
            print("Exiting the calculator. Goodbye!")
            break

        
        if operation in {'1', '2', '3', '4'}:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == '1':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == '2':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == '3':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif operation == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation choice. Please select a valid option (1/2/3/4/5).")

# Call the calculator function to run the program
calculator()
