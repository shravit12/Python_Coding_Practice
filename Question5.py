
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_pos_neg_zero(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def check_divisible(num):
    if num % 5 == 0 and num % 11 == 0:
        return "Yes (Divisible by both 5 and 11)"
    else:
        return "No"


def check_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not Prime"
    return "Prime"


def check_armstrong(num):
    if num < 0:
        return "Not Armstrong (Negative numbers are not Armstrong)"
    
    num_str = str(num)
    power = len(num_str)
    total_sum = sum(int(digit) ** power for digit in num_str)
    
    if total_sum == num:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"


while True:
        try:
            
            number = int(input("Enter an integer to analyze: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

even_odd = check_even_odd(number)
pos_neg = check_pos_neg_zero(number)
div = check_divisible(number)
prime = check_prime(number)
armstrong = check_armstrong(number)

   

print(f" Result\n\nAnalyzer Number: {number}\nEven/Odd : {even_odd}\nSign: {pos_neg}")
print(f"Divisible by 5 and 11 : {div}\nPrime Status : {prime}\nArmstrong Status: {armstrong}")



