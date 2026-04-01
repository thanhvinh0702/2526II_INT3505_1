from flask import Blueprint, request, jsonify
from models import db, User

author_bp = Blueprint("authors", __name__, url_prefix="/api/v1/authors")

# GET /api/v1/authors
@author_bp.route("", methods=["GET"])
def get_authors():
    query = User.query.filter(User.role == "AUTHOR")
    search = request.args.get("search")
    limit = request.args.get("limit", 10)
    offset = request.args.get("offset", 0)

    if search:
        query = query.filter(User.name.ilike(f"%{search}%"))
    total = query.count()
    authors = query.limit(limit).offset(offset).all()
    return jsonify({
        "data": [
            {
                "id": a.id,
                "name": a.name
            } for a in authors
        ],
        "pagination": {
            "total": total,
            "limit": limit,
            "offset": offset
        }
    })