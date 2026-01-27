"""
Exception-Safe Calculator
Handles invalid input and division errors gracefully
"""

def safe_input(prompt, input_type=float):
    """
    Safely get input from user with type validation
    
    Args:
        prompt (str): Prompt message
        input_type (type): Expected type (int or float)
    
    Returns:
        float/int: Valid user input
    """
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print(f"❌ Invalid input! Please enter a valid {input_type.__name__}")
        except KeyboardInterrupt:
            print("\n\n⚠️ Operation cancelled by user")
            return None


def add(a, b):
    """Add two numbers"""
    try:
        return a + b
    except Exception as e:
        print(f"❌ Error in addition: {e}")
        return None


def subtract(a, b):
    """Subtract two numbers"""
    try:
        return a - b
    except Exception as e:
        print(f"❌ Error in subtraction: {e}")
        return None


def multiply(a, b):
    """Multiply two numbers"""
    try:
        return a * b
    except Exception as e:
        print(f"❌ Error in multiplication: {e}")
        return None


def divide(a, b):
    """Divide two numbers with zero division handling"""
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b
    except ZeroDivisionError as e:
        print(f"❌ Division Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error in division: {e}")
        return None


def power(a, b):
    """Raise a to the power of b"""
    try:
        result = a ** b
        
        # Check for overflow
        if result == float('inf'):
            raise OverflowError("Result is too large!")
        
        return result
    except OverflowError as e:
        print(f"❌ {e}")
        return None
    except Exception as e:
        print(f"❌ Error in power operation: {e}")
        return None


def modulus(a, b):
    """Calculate modulus (remainder)"""
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulus with zero!")
        return a % b
    except ZeroDivisionError as e:
        print(f"❌ Modulus Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error in modulus operation: {e}")
        return None


def square_root(a):
    """Calculate square root"""
    try:
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return a ** 0.5
    except ValueError as e:
        print(f"❌ {e}")
        return None
    except Exception as e:
        print(f"❌ Error in square root: {e}")
        return None


def calculate(operation, a, b=None):
    """
    Perform calculation based on operation
    
    Args:
        operation (str): Operation to perform
        a (float): First number
        b (float): Second number (optional for some operations)
    
    Returns:
        float: Result of calculation
    """
    try:
        operations = {
            '+': lambda: add(a, b),
            '-': lambda: subtract(a, b),
            '*': lambda: multiply(a, b),
            '/': lambda: divide(a, b),
            '**': lambda: power(a, b),
            '%': lambda: modulus(a, b),
            'sqrt': lambda: square_root(a)
        }
        
        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")
        
        return operations[operation]()
    
    except Exception as e:
        print(f"❌ Calculation error: {e}")
        return None


def display_menu():
    """Display calculator menu"""
    print("\n" + "=" * 50)
    print("  🔢 EXCEPTION-SAFE CALCULATOR")
    print("=" * 50)
    print("  Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (**)")
    print("  6. Modulus (%)")
    print("  7. Square Root (√)")
    print("  8. Exit")
    print("=" * 50)


def main():
    """Main calculator function"""
    print("Welcome to Exception-Safe Calculator!")
    
    while True:
        try:
            display_menu()
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '8':
                print("\n👋 Thank you for using the calculator!")
                break
            
            operation_map = {
                '1': '+',
                '2': '-',
                '3': '*',
                '4': '/',
                '5': '**',
                '6': '%',
                '7': 'sqrt'
            }
            
            if choice not in operation_map:
                print("❌ Invalid choice! Please enter 1-8")
                continue
            
            operation = operation_map[choice]
            
            # Get first number
            num1 = safe_input("Enter first number: ", float)
            if num1 is None:
                continue
            
            # Get second number (not needed for square root)
            if operation == 'sqrt':
                result = calculate(operation, num1)
            else:
                num2 = safe_input("Enter second number: ", float)
                if num2 is None:
                    continue
                result = calculate(operation, num1, num2)
            
            # Display result
            if result is not None:
                print(f"\n✅ Result: {result}")
                
                # Format nicely for whole numbers
                if isinstance(result, float) and result.is_integer():
                    print(f"   (or {int(result)} as integer)")
        
        except KeyboardInterrupt:
            print("\n\n⚠️ Calculator interrupted. Goodbye!")
            break
        
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            print("Please try again.")


# Additional function: History tracking (bonus feature)
def calculator_with_history():
    """Calculator that keeps track of calculation history"""
    history = []
    
    print("Welcome to Calculator with History!")
    print("Type 'history' to see past calculations")
    print("Type 'clear' to clear history")
    
    while True:
        try:
            display_menu()
            
            choice = input("\nEnter choice (1-8, 'history', 'clear'): ").strip().lower()
            
            if choice == 'history':
                if not history:
                    print("\n📭 No history yet!")
                else:
                    print("\n📊 Calculation History:")
                    print("=" * 50)
                    for i, record in enumerate(history, 1):
                        print(f"{i}. {record}")
                    print("=" * 50)
                continue
            
            if choice == 'clear':
                history.clear()
                print("✅ History cleared!")
                continue
            
            if choice == '8':
                print("\n👋 Goodbye!")
                break
            
            operation_map = {
                '1': '+', '2': '-', '3': '*',
                '4': '/', '5': '**', '6': '%', '7': 'sqrt'
            }
            
            if choice not in operation_map:
                print("❌ Invalid choice!")
                continue
            
            operation = operation_map[choice]
            
            num1 = safe_input("Enter first number: ", float)
            if num1 is None:
                continue
            
            if operation == 'sqrt':
                result = calculate(operation, num1)
                if result is not None:
                    history.append(f"√{num1} = {result}")
                    print(f"\n✅ Result: {result}")
            else:
                num2 = safe_input("Enter second number: ", float)
                if num2 is None:
                    continue
                
                result = calculate(operation, num1, num2)
                if result is not None:
                    history.append(f"{num1} {operation} {num2} = {result}")
                    print(f"\n✅ Result: {result}")
        
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    # Run basic calculator
    main()
    
    # Uncomment to run calculator with history
    # calculator_with_history()