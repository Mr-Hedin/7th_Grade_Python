"""
Lesson 3: Calculating Averages
Learn how to find the average (mean) of a group of numbers.
"""
def instructions():
    print("Let's practice calculating averages.")
    print("To calculate an average:")
    print("1. Add all the numbers together")
    print("2. Divide by how many numbers there are")
    print("\nExample: For numbers [10, 20, 30]")
    print("1. Sum = 10 + 20 + 30 = 60")
    print("2. Count = 3 numbers")
    print("3. Average = 60 ÷ 3 = 20")


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average


print("Let's practice calculating averages.")
numbers = []

while True:
    print("\nCurrent numbers:", numbers)
    if numbers:
        print("Current average:", calculate_average(numbers))
    
    number = float(input("\nEnter a number (or 0 to finish): "))
    
    if number == 0:
        print("\nFinal Results:")
        print("Numbers entered:", numbers)
        print("Average:", calculate_average(numbers))
        print("Number of values:", len(numbers))
        print("Sum of values:", sum(numbers))
        break
        
    numbers.append(number)


