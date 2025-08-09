"""
Lesson 2: Seek
In this lesson you will learn about the file's pointer and how to navigate the data in your files.

.seek(0) - sends your pointer back to the beginning of the file
"""

# Create a sample story file
with open("story.txt", "w") as file:
    file.write("Once upon a time, there was a young programmer.\n")
    file.write("They loved to write code and solve problems.\n")
    file.write("Every day, they learned something new until their brain grew so large they could no longer move.\n")

# Read only the first 20 characters
with open("story.txt", "r") as file:
    
    print("First 20 characters:")
    start = file.read(20)
    print(start)

    # Move back to the beginning of the file
    print("\nMoving back to the start...")
    file.seek(0)

    # Read the next 10 characters
    print("\nNext 10 characters:")
    middle = file.read(10)
    print(middle)


# Practice Exercise:
print("1. Open the story.txt file")
print("2. Read the first 15 characters")
print("3. Use seek(0) to go back to the start")
print("4. Read the next 25 characters")
print("5. Close the file") 
