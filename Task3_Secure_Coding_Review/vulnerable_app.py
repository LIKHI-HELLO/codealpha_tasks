import sqlite3

# Hardcoded Credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")

# Sample User
cursor.execute("""
INSERT INTO users(username,password)
VALUES('likitha','password123')
""")

conn.commit()

print("=== Vulnerable Login System ===")

username = input("Username: ")
password = input("Password: ")

# SQL Injection Vulnerability
query = (
    "SELECT * FROM users WHERE username='"
    + username +
    "' AND password='"
    + password + "'"
)

try:
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Login Successful")
    else:
        print("Invalid Credentials")

except Exception as e:
    # Detailed Error Message
    print("Database Error:", e)

conn.close()
