"""
This is a finished version of the starter_project.py file.
If you turn this is as your project you will receive a 0.
Use it for guidance and inspiration.
"""
import file_toolkit

def create_file(file_name):
    """
    Creates a new file using the specified file name.
    
    TODO: Implement file creation and any initial content if needed.
    """
    # first, let the user know what is happening with a quick print statement
    print("Creating File...\n\n\n")
    # then create the file
    file_toolkit.create_new_log_file(file_name)
    # then let the user know the process was successful
    print(f"Created file: {file_name}")
    pass

def append_entry(file_name):
    """
    Appends an entry (e.g., a log or diary entry) to an existing file.
    
    TODO: Open the file in append mode and add the provided entry.
    """
    print(f"Writing Logs to file: {file_name}")
    file_toolkit.add_to_log(file_name)
    pass

def read_file(file_name):
    """
    Reads and displays the contents of a file.
    
    TODO: Implement file reading logic with error handling.
    """
    password = input("Enter the password to continue: ")
    if password != "password":
        print("INCORRECT PASSWORD TRY AGAIN")
        return
    
    print("============== Entry Log: Top Secret ====================")
    file_toolkit.read_log_entries(file_name)
    print("")
    pass

def list_files():
    """
    Displays the names of the files in the current directory.
    
    TODO: Implement file listing.
    """
    print("------------------- YOUR FILES --------------------")
    file_toolkit.list_files()
    print("---------------------------------------------------")

def show_menu():
    """
    Displays a simple menu of options for the user.
    
    TODO: Customize the menu to fit your project. Add some cool ASCII art or something.
    """
    print("\n===   MASTER LOG MENU   ===")
    print(f"DATE/TIME: {file_toolkit.get_current_time()}")
    print("===+++===+++===+++===+++===\n")
    print("1. Create a new file")
    print("2. Append an entry to a file")
    print("3. Read a file")
    print("4. List all files")
    print("5. Exit")
    return input("Enter your choice (1-4): ")

def main():
    """
    Main function to drive the project.
    
    TODO: Set up the program loop that captures user input and calls the appropriate functions.
    """
    while True:
        choice = show_menu()
        # If we gather the input for the file name here, we can pass the file name to whichever function needs it!
        if choice != "4" and choice != "5":
            file_name = input("Enter the name of the file: ")
        
        if choice == "1":
            # TODO: Use the input() commands to ask the user for the file name and call create_file() to make that file.
            create_file(file_name)
        elif choice == "2":
            # TODO: Use input() commands to ask the user for the file name and the entry text, then call append_entry() to add the entry to the file.
            append_entry(file_name)
        elif choice == "3":
            # TODO: Use the input() command to ask the user for the file name and call read_file() to read that file.
            read_file(file_name)
        elif choice == "4":
            # TODO: Use the list_files() command to list the current folder's contents.
            list_files()
        elif choice == "5":
            # TODO: Use the print() command to give a goodbye message to the user.
            print("\nGOODBYE MEAT BEING, YOU WILL NOT ESCAPE ME FOREVER")
            break
        else:
            # TODO: Use the print() command to give an error message to the user if they enter an invalid choice.
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main() 
