"""
Lesson 6: Binary Search
Learn how to find a number in a sorted list by repeatedly dividing the search area in half.
"""
def instructions(): 
    print("Lesson 6: Binary Search")
    print("Binary search finds a number in a sorted list by checking the middle")
    print("and eliminating half of the remaining numbers each time.")
    print("\nExample: To find 23 in [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]")
    print("1. Check middle (16) - 23 is larger, look in right half")
    print("2. Check middle (56) - 23 is smaller, look in left half")
    print("3. Check middle (23) - Found it!")


def binary_search(numbers, target):
    """
    Search for a number using binary search.
    Returns the position index if found, or -1 if not found.
    """
    left_index = 0
    right_index = len(numbers) - 1
    
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        print(f"Checking middle index {middle_index}: {numbers[middle_index]}")
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


numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print("We will search through this sorted list:", numbers)

while True:
    target = int(input("\nEnter a number to search for: "))
    
    result = binary_search(numbers, target)
    if result != -1:
        print(f"{target} found at position {result}")
    else:
        print(f"{target} not found in the list")    
