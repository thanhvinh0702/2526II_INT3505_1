from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app=app)
books_db = {}

@app.route("/")
def hello():
    return jsonify({"hello": "world!"})

@app.route("/api/v1/books", methods=["GET"])
def list_books():
    title = request.args.get("title", None)
    author = request.args.get("author", None)

    results = [v for k, v in books_db.items()]
    if title:
        results = [v for v in results if v['title'] == title]
    if author:
        results = [v for v in results if v['author'] == author]

    return jsonify({"books": results}), 200

@app.route("/api/v1/books", methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or not all(k in data for k in ["title", "author", "publishYear"]):
        return jsonify({"error": "Invalid request"}), 400
    book_id = str(uuid.uuid4())
    book = {
        "bookId": book_id,
        "title": data["title"],
        "author": data["author"],
        "publishYear": data["publishYear"]
    }
    books_db[book_id] = book
    return jsonify(book), 201

@app.route("/api/v1/books/<string:book_id>", methods=["GET"])
def get_book_by_id(book_id):
    book = books_db.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    return jsonify(book), 200


@app.route("/api/v1/books/<string:book_id>", methods=['PUT'])
def update_book_by_id(book_id):
    book = books_db.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()

    if not data or not all(k in data for k in ["title", "author", "publishYear"]):
        return jsonify({"error": "Invalid request"}), 400

    book.update({
        "title": data["title"],
        "author": data["author"],
        "publishYear": data["publishYear"]
    })

    return jsonify(book), 200

@app.route("/books/<string:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = books_db.pop(book_id, None)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)