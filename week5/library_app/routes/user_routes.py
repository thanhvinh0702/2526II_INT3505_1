from flask import Blueprint, request, jsonify
from models import db, User

user_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")

@user_bp.route("", methods=["POST"])
def create_user():
    data = request.json

    user = User(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"})