"""
Lesson 5: My Personal Diary
A practical application using everything we've learned about files.
"""

from datetime import datetime

def show_menu():
    print("\n=== My Personal Diary ===")
    print("1. Read my diary")
    print("2. Add new entry")
    print("3. Exit")
    return input("Choose an option (1-3): ")

def add_entry():
    print("\n=== New Diary Entry ===")
    entry = input("What happened today? ")
    
    # Open file in append mode and add the entry with date
    with open("my_diary.txt", "a") as file:
        current_date = datetime.now().strftime("%Y-%m-%d")
        file.write(f"\n[{current_date}]\n")
        file.write(entry + "\n")
        file.write("-" * 30 + "\n")
    
    print("Entry saved!")

def read_diary():
    print("\n=== My Diary Entries ===")
    try:
        with open("my_diary.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No entries yet!")
            else:
                print(content)
    except FileNotFoundError:
        print("No entries yet!")

# Main program
while True:
    choice = show_menu()
    
    if choice == "1":
        read_diary()
    elif choice == "2":
        add_entry()
    elif choice == "3":
        print("\nGoodbye! Your secrets are safe with us!... Not really. You should probably encrypt this file...")
        break
    else:
        print("\nPlease choose 1, 2, or 3") 
