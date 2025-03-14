from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # Enables fetching rows as dictionaries
    return conn

# Create users table if it doesn't exist
def create_table():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

create_table()  # Ensure the table is created when the app starts

# Route to get all users
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    
    return jsonify([dict(user) for user in users])

# Route to add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Invalid data"}), 400

    name = data["name"]
    age = data["age"]

    conn = get_db_connection()
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

    return jsonify({"message": "User added successfully!", "user": {"name": name, "age": age}}), 201

# Route to update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Invalid data"}), 400

    name = data["name"]
    age = data["age"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User updated successfully!", "user": {"id": user_id, "name": name, "age": age}})

# Route to delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted successfully!"})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)