from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "role": "admin"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "role": "user"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "role": "user"},
    {"id": 4, "name": "David", "email": "david@example.com", "role": "user"},
    {"id": 5, "name": "Eva", "email": "eva@example.com", "role": "admin"}
]

'''
Initial api, return {"id", "name", "email"}
'''
# @app.route("/api/v1/users")
# def get_users_init():
#     # Return the old format exactly
#     basic_users = [{"id": u["id"], "name": u["name"], "email": u["email"]} for u in users]
#     return jsonify({"data": basic_users})


'''
Extended api, allow filter by role and pagination. But still work with old client (Backward compatible)
'''
@app.route("/api/v1/users")
def get_users():

    result = users.copy()

    role = request.args.get("role")
    if role:
        result = [{"id": u["id"], "name": u["name"], "email": u["email"]} for u in result if u["role"] == role]

    # Optional pagination
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", len(result)))

    start = (page - 1) * limit
    end = start + limit

    paginated = result[start:end]

    response = {
        "data": paginated,
        "meta": {
            "total": len(result),
            "page": page,
            "limit": limit
        }
    }

    return jsonify(response)


users_v2 = [
    {"id": 1, "full_name": "Alice Johnson", "email": "alice@example.com", "role": "admin"},
    {"id": 2, "full_name": "Bob Scarllet", "email": "bob@example.com", "role": "user"},
    {"id": 3, "full_name": "Charlie Chaplin", "email": "charlie@example.com", "role": "user"},
    {"id": 4, "full_name": "David Beak", "email": "david@example.com", "role": "user"},
    {"id": 5, "full_name": "Eva 01", "email": "eva@example.com", "role": "admin"}
]

'''
New version api, break old structure -> not compatible with old client -> new version -> old client can still use old version
'''
@app.route("/api/v2/users")
def get_users_v2():
    v2_users = [{"id": u["id"], "full_name": u["full_name"], "email": u["email"]} for u in users_v2]
    return jsonify({"data": v2_users})


if __name__ == "__main__":
    app.run(debug=True)