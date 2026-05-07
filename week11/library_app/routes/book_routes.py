from flask import Blueprint, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from models import db, Book, User
from utils.jwt import require_jwt
import logging

book_bp = Blueprint("books", __name__, url_prefix="/api/v1/books")

logger = logging.getLogger(__name__)

# Rate Limitter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

@book_bp.record_once
def on_load(state):
    limiter.init_app(state.app)

@book_bp.route("", methods=["GET"])
@limiter.limit("5 per minute")
@require_jwt()
def get_books(claims):
    logger.info("Fetching all books")
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

    logger.info(f"Creating books: {data}")

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