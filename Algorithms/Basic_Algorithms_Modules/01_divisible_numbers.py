"""
Lesson 1: Divisible Numbers
Learn when one number can be divided evenly by another number.
"""

def is_divisible(number, divisor):
    """Check if a number is divisible by another number."""
    return number % divisor == 0

def check_divisibility():
    print("Let's check if numbers are divisible by 2, 3, or 5.")
    
    try:
        number = int(input("Enter a number to check: "))
        
        # Check divisibility by 2
        if is_divisible(number, 2):
            print(f"{number} is divisible by 2")
        else:
            print(f"{number} is not divisible by 2")
            
        # Check divisibility by 3
        if is_divisible(number, 3):
            print(f"{number} is divisible by 3")
        else:
            print(f"{number} is not divisible by 3")
            
        # Check divisibility by 5
        if is_divisible(number, 5):
            print(f"{number} is divisible by 5")
        else:
            print(f"{number} is not divisible by 5")
            
    except ValueError:
        print("Please enter a valid whole number.")

if __name__ == "__main__":
    print("Lesson 1: Divisible Numbers")
    print("A number is divisible by another number if there is no remainder.")
    print("Example: 6 is divisible by 2 because 6 ÷ 2 = 3 (no remainder)")
    print("Example: 7 is not divisible by 2 because 7 ÷ 2 = 3 remainder 1")
    
    while True:
        check_divisibility()
        again = input("\nWould you like to check another number? (yes/no): ")
        if again.lower() != 'no':
            break 
