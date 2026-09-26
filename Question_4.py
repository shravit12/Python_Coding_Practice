def verify(PIN):
    if PIN == 1234:
        print("Valid PIN! \n")
        return True 
    else:
        print("Wrong PIN Try Again!")
        return False 

def check_balance(balance):
    print(f"\n[Current Balance]: ₹{balance}")

def deposit(balance):
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            
       
            if amount < 10:
                print("Deposit must be minimum 10! Please try again.")
                continue  
                
            balance += amount
            print(f"Successfully Deposited! Updated Balance: ₹{balance}")
            return balance
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")
           

def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
            return balance
        if amount > balance:
            print("Insufficient fund.")
            return balance
        balance -= amount
        print(f"Successfully Withdrawn! Updated Balance: ₹{balance}")
        return balance
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return balance




while True:
        try:
            pin = input("Enter PIN (4 digits): ")
            if len(pin) != 4 or not pin.isdigit():
                print("Not Valid Value (4 digits hone chahiye)")
                continue  
            
            PIN = int(pin)
            if verify(PIN):
                break  
        except ValueError:
            print("Not Valid Value")
   
    # Initial Balance Validation Loop

while True:
        try:
            balance = float(input("Enter Initial Balance: "))
            if balance > 10**12:
                print("Balances is so Higher! Limit exceeded.")
                continue 
            if balance < 0:
                print("Balance cannot be negative.")
                continue
            break  
        except ValueError: 
            print("Please Enter Numbers Only")

    # ATM Menu Loop

while True:
        
        print("\n  ATM  ")
        
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print("\nThank you.")
            break
        else:
            print("Invalid choice! Please select between 1 to 4.")

