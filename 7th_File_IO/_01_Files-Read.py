"""
Lesson 1: Opening and Reading Files
Learn how to open and read a simple text file.
"""

# First, let's create a simple text file to work with
with open("my_first_file.txt", "w") as file:

    steps = "\nHere are the steps to write a file:\n"

    steps += "1. Open the file using the open() function with the mode 'w' for writing\n"
    steps += "2. Write to the file using the write() method\n"
    steps += "3. Close the file to tidy up\n"

    steps += "\nHere are the steps to read a file:\n"

    steps += "1. Open the file using the open() function with the mode 'r' for reading\n"
    steps += "2. Read its contents to a variable using the read() method\n"
    steps += "3. Close the file to tidy up\n"
    steps += "4. Print what you read\n"
    steps += "Day 77: They still don't know that I'm actually an octopus in a human suit."

    file.write(steps)




# Now let's learn to open and read the file
print("Reading the entire file at once:")

# First, we open the file
file = open("my_first_file.txt", "r")
# Then we read the file
content = file.read()
# Finally, we print the content
print(content)
# And close the file
file.close()

print("\nRemember: Always close your files when you're done!")


# The best way to read a file is to use a with statement - it will automatically close the file for you!
with open("my_first_file.txt", "r") as file:
    content = file.read()
    print(content)







