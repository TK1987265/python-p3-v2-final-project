
from lib.database import SessionLocal, init_db
from lib.models import Team, Wrestler

def main_menu():
    print("Welcome to Wrestling Management System!")
    # Implement menu options here for managing teams and wrestlers.

if __name__ == "__main__":
    init_db()
    main_menu()
