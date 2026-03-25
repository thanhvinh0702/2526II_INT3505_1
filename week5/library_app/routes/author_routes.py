from flask import Blueprint, request, jsonify
from models import db, Author

author_bp = Blueprint("authors", __name__, url_prefix="/api/v1/authors")

# POST /api/v1/authors
@author_bp.route("", methods=["POST"])
def create_author():
    data = request.json

    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    author = Author(name=data["name"])

    db.session.add(author)
    db.session.commit()

    return jsonify({
        "message": "Author created"
    })


# GET /api/v1/authors
@author_bp.route("", methods=["GET"])
def get_authors():
    authors = Author.query.all()

    return jsonify({
        "data": [
            {
                "id": a.id,
                "name": a.name
            } for a in authors
        ]
    })