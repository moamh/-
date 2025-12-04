def smart_calculator():
    print("--- Smart Calculator ---")

    while True:
        try:
            # 1. Input numbers
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))

            # 2. Choose operation
            print("Select Operation: (+, -, *, /, ^)")
            op = input("Enter symbol: ")

            result = None

            # 3. Calculation Logic
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            elif op == '^':
                result = num1 ** num2
            else:
                print("Invalid operation. Please try again.")
                continue

            # Display Result
            print(f"\nResult: {num1} {op} {num2} = {result}")

            # --- Extra Analysis ---
            
            # Compare numbers
            print("\n--- Analysis ---")
            if num1 > num2:
                print(f"First number ({num1}) is greater than second number ({num2}).")
            elif num1 < num2:
                print(f"First number ({num1}) is smaller than second number ({num2}).")
            else:
                print("Both numbers are equal.")

            # Check signs (Positive/Negative)
            def check_sign(n):
                if n > 0: return "Positive"
                elif n < 0: return "Negative"
                else: return "Zero"

            print(f"Number 1 is {check_sign(num1)}")
            print(f"Number 2 is {check_sign(num2)}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception:
            print("Something went wrong.")

        # Ask to continue
        again = input("\nDo you want to calculate again? (yes/no): ")
        if again.lower() not in ['yes', 'y']:
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    smart_calculator()
