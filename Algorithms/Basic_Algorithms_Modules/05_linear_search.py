"""
Lesson 5: Linear Search
Learn how to find an item in a list by checking each item one by one.
"""

def instructions():
    print("Let's practice linear search.")
    print("Linear search finds an item by checking each element one at a time.")
    print("It works on any list, even if it's not in order.")
    print("\nExample: To find 42 in [17, 3, 75, 42, 8]")
    print("1. Check 17 - not found")
    print("2. Check 3  - not found")
    print("3. Check 75 - not found")
    print("4. Check 42 - found!")

# Linear search algorithm
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


# Simple list of numbers to search through
numbers = [17, 3, 75, 42, 8, 21, 56, 93]

instructions()

while True:
    target = int(input("\nEnter a number to search for: "))
    result = linear_search(numbers, target)
    if result != -1:
        print(f"{target} found at position {result}")
    else:
        print(f"{target} not found in the list")



