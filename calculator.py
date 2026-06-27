import sys

def show_header():
    print("\n==================================================")
    print("               CODSOFT SMART CALCULATOR           ")
    print("==================================================")

def main():
    while True:
        try:
            show_header()
            
            # Get the first numerical value
            num1_input = input("Enter the first number (or type 'exit'): ").strip()
            if num1_input.lower() in ['exit', 'quit']:
                print("\nExiting Calculator. Goodbye!")
                break
            num1 = float(num1_input)
            
            # Get the second numerical value
            num2_input = input("Enter the second number: ").strip()
            num2 = float(num2_input)
            
            # Present mathematical operations choices
            print("\nSelect Operation:")
            print(" +  for Addition")
            print(" -  for Subtraction")
            print(" * for Multiplication")
            print(" /  for Division")
            operation = input("Enter choice (+, -, *, /): ").strip()
            
            print("--------------------------------------------------")
            
            # Calculation execution logic
            if operation == '+':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = \033[1;32m{result}\033[0m")
            elif operation == '-':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = \033[1;32m{result}\033[0m")
            elif operation == '*':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = \033[1;32m{result}\033[0m")
            elif operation == '/':
                if num2 == 0:
                    print("\033[1;31mError: Mathematical Division by Zero is undefined.\033[0m")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = \033[1;32m{result}\033[0m")
            else:
                print("\033[1;31mError: Invalid operator symbol chosen.\033[0m")
                
            print("==================================================")
            
        except ValueError:
            print("\033[1;31mError: Invalid input. Please enter valid numerical values.\033[0m")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()