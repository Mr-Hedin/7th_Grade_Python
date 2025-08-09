"""
Lesson 2: Adding Numbers and Finding Sums
Learn how to add multiple numbers together.
"""


# Basic Algorithm
def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total







numbers = []
# Use our summing algorithm to create a small program
while True:
    
    print("\nCurrent numbers:", numbers)
    
    number = int(input("\nEnter a number (or 0 to finish): "))

    # if the user enters a 0, exit the while True loop and print the results
    if number == 0:
        print("\nFinal Results:")
        print("Numbers entered:", numbers)
        print("Total sum:", calculate_sum(numbers))
        print("Number of values added:", len(numbers))
        numbers = []
        break
        
    numbers.append(number)
