"""
Lesson 4: Creating an Interactive Log
Learn how to create a set of tools that can be used to create a program!
In this lesson, you'll practice creating functions that manage log entries 
interactively and see how file pointers work when reading files.
"""
import os
from datetime import datetime
# First, create a new file based on user input
file_name = input("Enter the name of the file to create: ")

def list_files():
    # List all files in the current directory
    files = os.listdir()
    print("Files in the current directory:")
    for file in files:
        print(file)


def create_new_log_file(file_name):
    # Create the file if it doesn't exist
    if not os.path.exists(file_name):   
        with open(file_name, "w") as file:
            file.write("Interactive Log Start:\n")
    


def add_to_log(file_name):
    # Inform the user
    print("Enter your log entries. Type 'exit' to finish adding entries.")
    # Append new entries to the log file using file append mode ('a')
    with open(file_name, "a") as file:
        while True:
            entry = input("Log entry (type 'exit' to finish): ")
            if entry.strip().lower() == "exit":
                break
            file.write(entry + "\n")

def read_log_entries(file_name):
    # Read and display the log entries using seek and readline
    print("\nReading log entries using seek and readline:")
    with open(file_name, "r") as file:
        file.seek(0)  # make sure the file pointer is at the beginning
        for line in file:
            print(line)
        print("done")
    
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def read_list(file_name):
    print("generating list of lines from the file...")
    with open(file_name, "r") as file:
        lines = file.readlines()
    return lines


# Practice Exercise:
# Using the code above, create a new log file and add some entries to it.
# Then, read the entries and display them.  
# Try using some of the functions and seeing what they return/do exactly!
create_new_log_file(file_name)
print(get_current_time())
print(read_list(file_name))




 
