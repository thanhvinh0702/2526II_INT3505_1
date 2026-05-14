from flask import Blueprint, request, jsonify
from models import db, User
from utils.jwt import create_access_token
import logging

user_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")
logger = logging.getLogger(__name__)

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter(User.email == data["email"], User.password == data["password"]).first()
    if user == None:
        logger.warning("Login failed for email=%s", data["email"])
        return jsonify({"message": "Invalid email or password"}), 404
    access_token = create_access_token(
        sub=user.id,
        role=user.role
    )
    logger.info("Login succeeded for user_id=%s role=%s", user.id, user.role)
    return jsonify({"access_token": access_token})

@user_bp.route("/signup", methods=["POST"])
def create_user():
    data = request.json
        
    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"],
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    logger.info("User created with user_id=%s role=%s", user.id, user.role)

    return jsonify({"message": "User created"})
