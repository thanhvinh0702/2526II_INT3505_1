from flask import Blueprint, request, jsonify
from models import db, Book, Author, Category

book_bp = Blueprint("books", __name__, url_prefix="/api/v1/books")

@book_bp.route("", methods=["GET"])
def get_books():
    search = request.args.get("search")
    author_id = request.args.get("author_id")
    category_id = request.args.get("category_id")
    limit = int(request.args.get("limit", 10))
    offset = int(request.args.get("offset", 0))
    query = Book.query

    if search:
        query = query.filter(Book.title.ilike(f"%{search}%"))

    if author_id:
        query = query.filter(Book.author_id == author_id)

    if category_id:
        query = query.filter(Book.category_id == category_id)

    total = query.count()
    books = query.offset(offset).limit(limit).all()

    result = []
    for b in books:
        result.append({
            "id": b.id,
            "title": b.title,
            "author": b.author.name if b.author else None,
            "category": b.category.name if b.category else None
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
def create_book():
    data = request.json

    author_id = data.get("author_id")
    category_id = data.get("category_id")

    author = Author.query.get(author_id)
    category = Category.query.get(category_id)

    if not author:
        return jsonify({
            "error": "Author not found"
        }), 400

    if not category:
        return jsonify({
            "error": "Category not found"
        }), 400

    book = Book(
        title=data["title"],
        author_id=author_id,
        category_id=category_id,
        available_copies=data.get("available_copies", 1)
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book created"})