import math

def calculator():
    """A simple calculator in Python."""

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Trigonometric Functions (sin, cos, tan)")
        print("8. Quit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print("Result:", result)

        elif choice == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print("Result:", result)

        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print("Result:", result)

        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Result:", result)

        elif choice == '5':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = base ** exponent
            print("Result:", result)

        elif choice == '6':
            num = float(input("Enter a number: "))
            if num < 0:
                print("Error: Cannot take the square root of a negative number.")
            else:
                result = math.sqrt(num)
                print("Result:", result)

        elif choice == '7':
            angle = float(input("Enter the angle in degrees: "))
            angle_radians = math.radians(angle)
            print("Sine:", math.sin(angle_radians))
            print("Cosine:", math.cos(angle_radians))
            print("Tangent:", math.tan(angle_radians))

        elif choice == '8':
            print("Exiting calculator...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()