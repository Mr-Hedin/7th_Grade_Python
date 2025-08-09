# Algorithms File:
# This file contains a collection of algorithms that are commonly used in programming.
# These functions can be called in other files to perform various tasks.
# Think of it like a toolkit that you can build up over time.
# Many excellent programmers have built up their own toolkits of algorithms and data structures that they use in their projects.
# This is a structure to start building your own toolkit, eventually you could publish your own Python package to share with others!

def prepare_a_list():
    """Prepare the dataset for our algorithms. This writes to a file called 'numbers.txt'."""
    pass

# 1. Check if a number is divisible by another number.
def is_divisible(number, divisor):
    """Check if a number is divisible by another number."""
    return number % divisor == 0

# 2. Calculate the sum of a list of numbers.
def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total

# 3. Calculate the average of a list of numbers.
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

# 4. Find the smallest number in a list.
def find_min(numbers):
    """Find the smallest number in a list."""
    if not numbers:
        return None
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

# 5. Find the largest number in a list.
def find_max(numbers):
    """Find the largest number in a list."""
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def linear_search(items, target):
    """
    Search for an item in a list one by one.
    Returns the position (index) if found, or -1 if not found.
    """
    for index in range(len(items)):
        print("Checking position: ", index)
        if items[index] == target:
            print("Found at position: ", index)
            return index
        print("Not found, continuing search...")
    print("Not found")
    return -1

def binary_search(numbers, target):
    """
    Search for a number using binary search.
    Returns the position if found, or -1 if not found.
    """
    left_index = 0
    right_index = len(numbers) - 1
    
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        print(f"Checking middle position {middle_index}: {numbers[middle_index]}")
        if numbers[middle_index] == target:
            return middle_index
        elif numbers[middle_index] < target:
            print(f"{target} is larger, looking in right half")
            left_index = middle_index + 1
        else:
            print(f"{target} is smaller, looking in left half")
            right_index = middle_index - 1
    print(f"{target} not found in the list")
    return -1
