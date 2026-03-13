from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

SECRET_KEY = "SECRET_KEY"

users = [
            {'username': 'admin', 'password': '123123123', 'role': 'admin'}, 
            {'username': 'user', 'password': '123123123', 'role': 'user'}
        ]


def create_access_token(sub: str, role: str):
    now = datetime.datetime.utcnow()

    payload = {
        "sub": sub,
        "role": role,
        "iat": now,
        "exp": now + datetime.timedelta(minutes=30)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def parse_bearer_token():
    auth = request.headers.get("Authorization") or ""
    parts = auth.split()

    if len(parts) == 2 and parts[0].lower() == "bearer":
        return parts[1]

    return None


def require_jwt(required_role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            token = parse_bearer_token()

            if not token:
                return jsonify({"msg": "Missing token"}), 401

            try:
                claims = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

            except jwt.ExpiredSignatureError:
                return jsonify({"msg": "Token expired"}), 401

            except jwt.InvalidTokenError:
                return jsonify({"msg": "Invalid token"}), 401

            if required_role and claims.get("role") != required_role:
                return jsonify({"msg": "Forbidden"}), 403

            return f(claims, *args, **kwargs)

        return wrapper

    return decorator


@app.route("/api/v1/login", methods=["POST"])
def login():
    data = request.get_json()

    for user in users:
        if user["username"] == data["username"] and user["password"] == data["password"]:

            access_token = create_access_token(
                sub=user["username"],
                role=user['role']
            )

            return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401


@app.route("/api/v1/profile", methods=["GET"])
@require_jwt()
def profile(claims):
    return jsonify({
        "username": claims["sub"],
        "role": claims["role"]
    })


@app.route("/api/v1/admin", methods=["GET"])
@require_jwt("admin")
def admin(claims):
    return jsonify({
        "msg": "Welcome admin",
        "user": claims["sub"]
    })


if __name__ == "__main__":
    app.run(debug=True)