from flask import Blueprint, request, jsonify
from models import db, Category

category_bp = Blueprint("categories", __name__, url_prefix="/api/v1/categories")

# POST /api/v1/categories
@category_bp.route("", methods=["POST"])
def create_category():
    data = request.json

    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    category = Category(name=data["name"])

    db.session.add(category)
    db.session.commit()

    return jsonify({
        "message": "Category created"
    })


# GET /api/v1/categories
@category_bp.route("", methods=["GET"])
def get_categories():
    categories = Category.query.all()

    return jsonify({
        "data": [
            {
                "id": c.id,
                "name": c.name
            } for c in categories
        ]
    })