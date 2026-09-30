# Interactive Calculator & Unit Converter


# -----------------------------------
# Function to get a valid number
# -----------------------------------
def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# -----------------------------------
# Basic Arithmetic
# -----------------------------------
def arithmetic():
    while True:
        print("\n===== Basic Arithmetic =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = num1 + num2
            print("Result:", result)

        elif choice == "2":
            result = num1 - num2
            print("Result:", result)

        elif choice == "3":
            result = num1 * num2
            print("Result:", result)

        elif choice == "4":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Result:", result)


# -----------------------------------
# Unit Conversion
# -----------------------------------
def unit_conversion():
    while True:
        print("\n===== Unit Conversion =====")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "3":
            break

        if choice == "1":
            kilometers = get_number("Enter kilometers: ")

            if kilometers < 0:
                print("Distance cannot be negative.")
                continue

            miles = kilometers * 0.621371

            print("Miles:", round(miles, 2))

        elif choice == "2":
            celsius = get_number("Enter temperature in Celsius: ")

            fahrenheit = (celsius * 9 / 5) + 32

            print("Temperature in Fahrenheit:", round(fahrenheit, 2))

        else:
            print("Invalid choice! Please try again.")


# -----------------------------------
# Currency Conversion
# -----------------------------------
def currency_conversion():
    while True:
        print("\n===== Currency Conversion =====")
        print("1. USD to INR")
        print("2. INR to USD")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "3":
            break

        if choice == "1":
            usd = get_number("Enter amount in USD: ")

            if usd < 0:
                print("Amount cannot be negative.")
                continue

            # Example fixed exchange rate
            exchange_rate = 83

            inr = usd * exchange_rate

            print("Amount in INR:", round(inr, 2))

        elif choice == "2":
            inr = get_number("Enter amount in INR: ")

            if inr < 0:
                print("Amount cannot be negative.")
                continue

            # Example fixed exchange rate
            exchange_rate = 83

            usd = inr / exchange_rate

            print("Amount in USD:", round(usd, 2))

        else:
            print("Invalid choice! Please try again.")


# -----------------------------------
# Main Program
# -----------------------------------
def main():
    while True:
        print("\n==========================================")
        print("   INTERACTIVE CALCULATOR & CONVERTER")
        print("==========================================")

        print("1. Basic Arithmetic")
        print("2. Unit Conversion")
        print("3. Currency Conversion")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arithmetic()

        elif choice == "2":
            unit_conversion()

        elif choice == "3":
            currency_conversion()

        elif choice == "4":
            print("\nThank you for using the program!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


# -----------------------------------
# Start the Program
# -----------------------------------
if __name__ == "__main__":
    main()