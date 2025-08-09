"""
Lesson 4: Finding Minimum and Maximum Values
Learn how to find the smallest and largest numbers in a group.
"""

def find_min(numbers):
    """Find the smallest number in a list."""
    if not numbers:
        return None
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

def find_max(numbers):
    """Find the largest number in a list."""
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number




print("Let's practice finding minimum and maximum values.")
numbers = []

while True:
    print("\nCurrent numbers:", numbers)
    if numbers:
        print("Smallest number:", find_min(numbers))
        print("Largest number:", find_max(numbers))
    
    number = float(input("\nEnter a number (or 0 to finish): "))
    
    if number == 0:
        print("\nFinal Results:")
        print("Numbers entered:", numbers)
        print("Smallest number (minimum):", find_min(numbers))
        print("Largest number (maximum):", find_max(numbers))
        if len(numbers) >= 2:
            print("Difference between largest and smallest:", find_max(numbers) - find_min(numbers))
        break
        
    numbers.append(number)
