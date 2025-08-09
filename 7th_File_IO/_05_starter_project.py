"""
Project Starter for File I/O

This template provides the basic structure and function definitions.
Students should fill in the implementation details and expand on the functionality.
"""

def create_file(file_name):
    """
    Creates a new file using the specified file name.
    
    TODO: Implement file creation and any initial content if needed.
    """
    pass

def append_entry(file_name):
    """
    Appends an entry (e.g., a log or diary entry) to an existing file.
    
    TODO: Open the file in append mode and add the provided entry.
    """
    pass

def read_file(file_name):
    """
    Reads and displays the contents of a file.
    
    TODO: Implement file reading logic with error handling.
    """
    pass

def list_files():
    """
    Displays the names of the files in the current directory.
    
    TODO: Implement file listing.
    """

def show_menu():
    """
    Displays a simple menu of options for the user.
    
    TODO: Customize the menu to fit your project.
    """
    print("\n=== Project Menu ===")
    print("1. Create a new file")
    print("2. Append an entry to a file")
    print("3. Read a file")
    print("4. List available files")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def main():
    """
    Main function to drive the project.
    
    TODO: Set up the program loop that captures user input and calls the appropriate functions.
    """
    while True:
        choice = show_menu()
        if choice == "1":
            # TODO: Use the input() commands to ask the user for the file name and call create_file() to make that file.
            pass
        elif choice == "2":
            # TODO: Use input() commands to ask the user for the file name and the entry text, then call append_entry() to add the entry to the file.
            pass
        elif choice == "3":
            # TODO: Use the input() command to ask the user for the file name and call read_file() to read that file.
            pass
        elif choice == "4":
            # TODO: Use the print() command to add some formatting when you print your files. Call list_files() once you've completed it to print the filenames.
            pass
        elif choice == "5":
            # TODO: Use the print() command to give a goodbye message to the user.
            print("")
            break
        else:
            # TODO: Use the print() command to give an error message to the user if they enter an invalid choice.
            print("")

if __name__ == "__main__":
    main() 
