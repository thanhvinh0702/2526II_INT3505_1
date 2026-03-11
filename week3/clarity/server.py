from flask import Flask, jsonify

app = Flask(__name__)

mock_users = [
  { "id": 1, "name": "John" },
  { "id": 2, "name": "Claire" }
]

# Non clarity example. 
@app.route("/api/v1/data", methods=["GET"])
def get_data():
    return {"data": mock_users}

# Clarity example
@app.route("/api/v1/users", methods=["GET"])
def get_users():
    return {"data": mock_users}

@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in mock_users:
        if user['id'] == user_id:
            return {"data": user}
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)