def simple_calculator():
    
    try:
        num1 = float(input("Enter first number: "))
        oper = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if oper == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif oper == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif oper == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif oper == '/':
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operator! Please use +, -, *, or /.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def check_even_odd():
    print("\n--- Check Even / Odd ---")
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"Result: {num} is an **Even** number.")
        else:
            print(f"Result: {num} is an **Odd** number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def find_largest_of_three():
    print("\n--- Find Largest of Three Numbers ---")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
        
        largest = max(a, b, c)
        print(f"Result: The largest number among {a}, {b}, and {c} is **{largest}**.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")



def login_system():
    correct_user = "shravit"
    correct_pass = "sh@123"
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        print(f"\n--- Login Attempt ({attempts + 1}/{max_attempts}) ---")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        
        if username == correct_user and password == correct_pass:
            print("\n Login Successful! Welcome, Admin.")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Wrong username or password!")
            if remaining > 0:
                print(f"Attempts left: {remaining}")
                
    # Agar 3ron attempts fail ho jayein
    print("\n Account Locked! Too many failed login attempts.")
    return False


# --- 3. Main Program Execution ---

def main():
    # Pehle login check karein
    if not login_system():
        return  # Agar account lock ho gaya, toh program yhi stop ho jayega
        
    # Agar login successful hua, toh ATM/Tool ki tarah Menu dikhayenge
    while True:
        print("\n==================================")
        print("           MAIN MENU            ")
        print("==================================")
        print("1. Simple Calculator")
        print("2. Check Even/Odd")
        print("3. Find Largest of Three Numbers")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            simple_calculator()
        elif choice == '2':
            check_even_odd()
        elif choice == '3':
            find_largest_of_three()
        elif choice == '4':
            print("\nExiting program. Have a great day!")
            break
        else:
            print("Invalid choice! Please select between 1 to 4.")

# Program Start
if __name__ == "__main__":
    main()