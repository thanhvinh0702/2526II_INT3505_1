from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

def user_with_links(user):
    return {
        "id": user["id"],
        "name": user["name"],
        "_links": {
            "self": url_for("get_user", user_id=user["id"], _external=True),
            "update": url_for("update_user", user_id=user["id"], _external=True),
            "delete": url_for("delete_user", user_id=user["id"], _external=True),
            "all_users": url_for("get_users", _external=True)
        }
    }

@app.route("/api/v1/users/profile", methods=["GET"])
def get_profile():
    user_id = request.headers.get("X-USER-ID")
    if not user_id:
        return jsonify({"error": "No user"}), 401
    for user in users:
        if str(user["id"]) == user_id:
            return jsonify(user_with_links(user))
    return jsonify({"error": "User not found"}), 404

@app.route("/api/v1/users", methods=["GET"])
def get_users():
    return jsonify([user_with_links(u) for u in users])

@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user_with_links(user))
    return jsonify({"error": "User not found"}), 404

@app.route("/api/v1/users", methods=["POST"])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(user_with_links(new_user)), 201

@app.route("/api/v1/users/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user_with_links(user))
    return jsonify({"error": "User not found"}), 404

@app.route("/api/v1/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run(port=8080)