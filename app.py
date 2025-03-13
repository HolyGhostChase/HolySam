from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (acts as a temporary database)
users = []

# Route to get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Route to add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added successfully!", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)