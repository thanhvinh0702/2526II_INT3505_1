from flask import Blueprint, request, jsonify
from models import db, Loan, Book
from utils.jwt import require_jwt

loan_bp = Blueprint("loans", __name__, url_prefix="/api/v1/loans")

@loan_bp.route("", methods=["GET"])
@require_jwt()
def get_loans(claims):
    query = Loan.query.filter(Loan.user_id == claims['sub'])

    limit = request.args.get("limit", 10)
    offset = request.args.get("offset", 0)

    total = query.count()
    query = query.limit(limit).offset(offset)

    results = []
    for l in query:
        results.append({
            "id": l.id,
            "user_id": l.user_id,
            "book_id": l.book_id,
            "borrow_date": l.borrow_date,
            "return_date": l.return_date
        })
    return jsonify({
        "date": results,
        "pagination": {
            "total": total,
            "limit": limit,
            "offset": offset
        }})

@loan_bp.route("", methods=["POST"])
@require_jwt()
def borrow_book(claims):
    data = request.json

    book = Book.query.get(data["book_id"])

    if not book or book.available_copies <= 0:
        return jsonify({"error": "Book not available"}), 400

    loan = Loan(
        user_id=claims["sub"],
        book_id=data["book_id"]
    )

    book.available_copies -= 1

    db.session.add(loan)
    db.session.commit()

    return jsonify({"message": "Book borrowed"})


@loan_bp.route("/<int:id>/return", methods=["PATCH"])
@require_jwt()
def return_book(claims, id):
    loan = Loan.query.get(id)

    if not loan:
        return jsonify({"error": "Loan not found"}), 404

    loan.return_date = db.func.now()

    book = Book.query.get(loan.book_id)
    book.available_copies += 1

    db.session.commit()

    return jsonify({"message": "Book returned"})