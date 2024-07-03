
## Usage
# The application allows you to:
# - Create, view, and delete recipe categories.
# - Add, delete, and view recipes within those categories.


from lib.database import SessionLocal, init_db
from lib.models import Team, Wrestler
import sys


def main_menu():
    print("Welcome to Wrestling Management System!")
    print("1. Initialize Database")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        init_db()
    elif choice == '2':
        print("Exiting the application.")
        sys.exit(0)
    else:
        print("Invalid choice, please choose again.")
        main_menu()

if __name__ == "__main__":
    main_menu()
