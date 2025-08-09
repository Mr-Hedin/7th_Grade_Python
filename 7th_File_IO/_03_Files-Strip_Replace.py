"""
https://i.kym-cdn.com/photos/images/original/001/253/025/34d.jpg
Lesson 2: Reading Lines and Removing Whitespace
Learn how to read files line by line and clean up the text.
"""

with open("grocery_list.txt", "w") as file:
    file.write("            Apples                     \n")
    file.write("Bananas                      \n")
    file.write("    Oranges         \n")
    file.write("                                                           Milk\n")

with open("grocery_list.txt", "r") as file:
    # Use a for loop to read each line
    print("Original: ")
    for line in file:
        print(line)
        
    file.seek(0)

    # after resetting our location in the file, we can strip out the blank spaces!
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)

    file.seek(0)
    # This uses .replace("a", "e") instead of .strip() and prints the output to replace the letters in our words!
    for line in file:
        modified_line = line.replace("a", "e")
        print(modified_line)
 



print("\nTo read a file line by line, you can use a for loop")
print("To output the text in a readable format we can use several string methods like .strip()")
print(".strip() removes extra spaces or newline characters at the end of a string, this can be extremely useful for formatting!")
print("Instructions:")
print("1. Open the grocery_list.txt file")
print("2. Read each line and print it")
print("3. Seek the start of the file to reset where we're at in the file")
print("4. Remove extra spaces and newlines with .strip()")
print("5. Print the clean lines")
