from flask import Blueprint, request, jsonify
from models import db, Book, User
from utils.jwt import require_jwt

book_bp = Blueprint("books", __name__, url_prefix="/api/v1/books")

@book_bp.route("", methods=["GET"])
@require_jwt()
def get_books(claims):
    search = request.args.get("search")
    author_id = request.args.get("author_id")
    category = request.args.get("category")
    limit = int(request.args.get("limit", 10))
    offset = int(request.args.get("offset", 0))
    query = Book.query

    if search:
        query = query.filter(Book.title.ilike(f"%{search}%"))

    if author_id:
        query = query.filter(Book.author_id == author_id)

    if category:
        query = query.filter(Book.category == category)

    total = query.count()
    books = query.offset(offset).limit(limit).all()

    result = []
    for b in books:
        result.append({
            "id": b.id,
            "title": b.title,
            "author": b.author.name if b.author else None,
            "category": b.category if b.category else None
        })

    return jsonify({
        "data": result,
        "pagination": {
            "total": total,
            "limit": limit,
            "offset": offset
        }
    })

@book_bp.route("", methods=["POST"])
@require_jwt("AUTHOR")
def create_book(claims):
    data = request.json

    author = User.query.filter(
        User.id == claims["sub"],
        User.role == "AUTHOR"
    ).first()

    if not author:
        return jsonify({
            "error": "Author not found"
        }), 400

    book = Book(
        title=data["title"],
        author_id=author.id,
        category=data["category"],
        available_copies=data.get("available_copies", 1)
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book created"})