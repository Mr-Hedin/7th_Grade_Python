

import file_toolkit  # This imports our shared toolkit with functions like create_new_log_file and get_current_time

def create_new_creature_file(file_name):
    """
    Creates a new file for storing creature information.
    """
    file_toolkit.create_new_log_file(file_name)


def add_creature(file_name):
    """
    Prompts the user to input details about a mythical creature.
    Each creature is logged with its name, description, special ability, and the time it was created.
    """
    print("\nLet's create a mythical creature!")
    name = input("Enter the creature's name: ") # get the name from the user
    description = input("Describe your creature: ") # get the description from the user
    ability = input("Enter its special ability: ") # get the ability from the user
    timestamp = file_toolkit.get_current_time() # get the current time

    entry = f"[{timestamp}] Name: {name} | Description: {description} | Ability: {ability}\n" # create the entry with some fancy formatting

    with open(file_name, "a") as f: # open the file in append mode
        f.write(entry) # write the entry to the file
    print("Your creature has been added to the log!\n") # print a message to the user

def view_creatures(file_name):
    """
    Reads and displays all the mythical creature entries.
    """
    print("\n--- Mythical Creatures Log ---")
    file_toolkit.read_log_entries(file_name)
    print("-------------------------------\n")


# Here we create the main function that will run the program
# This is our app! We show the user a menu and they can choose what they want to do
# Each option is handled by a different function
# We also handle errors and edge cases like the user not entering a valid choice
def creature_creator_app():
    """
    Provides a simple menu interface for the Mythical Creature Creator.
    """
    file_name = input("Enter the name of your mythical creatures file: ")
    file_toolkit.create_new_log_file(file_name)

    while True:
        print("Mythical Creature Menu:")
        print("1. Create a new creature")
        print("2. View all creatures")
        print("3. List files in the directory")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_creature(file_name)
        elif choice == "2":
            view_creatures(file_name)
        elif choice == "3":
            file_toolkit.list_files()
        elif choice == "4":
            print("See you next time! Your horrific menagerie of nightmarish monstrosities is safe with us!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    creature_creator_app()