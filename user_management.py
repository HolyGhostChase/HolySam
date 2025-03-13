import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
""")

def add_user():
    """Add a new user"""
    name = input("Enter name: ")
    age = input("Enter age: ")

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(f"User {name} added!")

def view_users():
    """View all users"""
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if not users:
        print("No users found.")
    else:
        print("\nUser List:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")

while True:
    print("\nOptions:")
    print("1. Add User")
    print("2. View Users")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        view_users()
    elif choice == "3":
        print("Goodbye!")
        conn.close()
        break
    else:
        print("Invalid choice! Enter 1, 2, or 3.")