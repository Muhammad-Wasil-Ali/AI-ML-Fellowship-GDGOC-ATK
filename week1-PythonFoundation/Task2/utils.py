"""
Utility Functions Module
Contains reusable functions for common tasks
"""

def validate_email(email):
    """Validate if email has basic correct format"""
    if '@' in email and '.' in email.split('@')[1]:
        return True
    return False


def validate_phone(phone):
    """Validate phone number (removes spaces/dashes and checks if digits)"""
    cleaned = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    return cleaned.isdigit() and len(cleaned) >= 10


def capitalize_name(name):
    """Capitalize each word in a name"""
    return ' '.join(word.capitalize() for word in name.split())


def format_phone(phone):
    """Format phone number to standard format: (123) 456-7890"""
    digits = ''.join(filter(str.isdigit, phone))
    
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    return phone


def get_valid_input(prompt, validation_func=None, error_msg="Invalid input"):
    """Get input from user with validation"""
    while True:
        user_input = input(prompt).strip()
        
        if validation_func is None:
            return user_input
        
        if validation_func(user_input):
            return user_input
        else:
            print(f" {error_msg}")


def safe_int_input(prompt, min_val=None, max_val=None):
    """Get integer input from user with optional range validation"""
    while True:
        try:
            value = int(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f" Value must be at least {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f" Value must be at most {max_val}")
                continue
            
            return value
        
        except ValueError:
            print("Please enter a valid integer")


def safe_float_input(prompt, min_val=None, max_val=None):
    """Get float input from user with optional range validation"""
    while True:
        try:
            value = float(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f" Value must be at least {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f" Value must be at most {max_val}")
                continue
            
            return value
        
        except ValueError:
            print("Please enter a valid number")


def display_menu(title, options):
    """Display a formatted menu with options"""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)
    
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    
    print("=" * 50)


def confirm_action(prompt="Are you sure?"):
    """Ask user to confirm an action"""
    response = input(f"{prompt} (y/n): ").strip().lower()
    return response in ['y', 'yes']


def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"


# Test the utilities
if __name__ == "__main__":
    print("Testing Utility Functions\n")
    
    # Test email validation
    print("Email Validation:")
    print(f"test@example.com -> {validate_email('test@example.com')}")
    print(f"invalid-email -> {validate_email('invalid-email')}")
    
    # Test phone validation
    print("\nPhone Validation:")
    print(f"123-456-7890 -> {validate_phone('123-456-7890')}")
    print(f"12345 -> {validate_phone('12345')}")
    
    # Test phone formatting
    print("\nPhone Formatting:")
    print(f"1234567890 -> {format_phone('1234567890')}")
    print(f"11234567890 -> {format_phone('11234567890')}")
    
    # Test name capitalization
    print("\nName Capitalization:")
    print(f"john doe -> {capitalize_name('john doe')}")
    
    # Test currency formatting
    print("\nCurrency Formatting:")
    print(f"1234.56 -> {format_currency(1234.56)}")