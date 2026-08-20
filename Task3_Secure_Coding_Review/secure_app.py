import sqlite3
import bcrypt

DB_NAME = "users.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def validate_password(password):
    if len(password) < 8:
        return False
    return True


def register_user(username, password):

    if not validate_password(password):
        print("Password must contain at least 8 characters.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES (?,?)",
            (username, hashed_password)
        )

        conn.commit()
        print("User registered successfully.")

    except sqlite3.IntegrityError:
        print("Username already exists.")

    finally:
        conn.close()


def login_user(username, password):

    if not username.strip():
        print("Username cannot be empty.")
        return

    if len(username) > 30:
        print("Invalid username length.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT password FROM users WHERE username=?",
            (username,)
        )

        result = cursor.fetchone()

        if result:

            stored_hash = result[0]

            if bcrypt.checkpw(
                password.encode(),
                stored_hash.encode()
            ):
                print("Login Successful")
            else:
                print("Invalid Credentials")

        else:
            print("Invalid Credentials")

    except Exception:
        print("An error occurred. Please try again later.")

    finally:
        conn.close()


def main():

    create_database()

    print("\n=== Secure Login System ===")

    print("1. Register")
    print("2. Login")

    choice = input("Enter Choice: ")

    username = input("Username: ")
    password = input("Password: ")

    if choice == "1":
        register_user(username, password)

    elif choice == "2":
        login_user(username, password)

    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()
