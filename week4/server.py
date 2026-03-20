from flask import Flask, request, jsonify, abort
import uuid
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)

SWAGGER_URL = "/docs"
API_URL = "/api_doc.yaml"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Book Management API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Serve your YAML file
from flask import send_from_directory
@app.route("/api_doc.yaml")
def swagger_yaml():
    return send_from_directory(".", "api_doc.yaml")

books_db = {}


@app.route("/", methods=['GET'])
def hello():
    return jsonify({"hello": "world"}), 200

@app.route("/books", methods=["GET"])
def list_books():
    title = request.args.get("title")

    result = list(books_db.values())

    if title:
        result = [b for b in result if title.lower() in b["title"].lower()]

    return jsonify({"books": result}), 200

@app.route("/books", methods=["POST"])
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

@app.route("/books/<book_id>", methods=["GET"])
def get_book(book_id):
    book = books_db.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book), 200

@app.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
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

@app.route("/books/<book_id>", methods=["PATCH"])
def patch_book(book_id):
    book = books_db.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    # Update only provided fields
    for field in ["title", "author", "publishYear"]:
        if field in data:
            book[field] = data[field]

    return jsonify(book), 200


@app.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = books_db.pop(book_id, None)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)