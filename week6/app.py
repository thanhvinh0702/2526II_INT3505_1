from flask import Flask, request, jsonify
import sqlite3
import time

app = Flask(__name__)

DB = "books.db"


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS books")
    cur.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    """)

    print("Seeding data...")
    data = []
    for _ in range(1000000):
        data.append((
            "Test Book",
            "Test Author",
            2006
        ))

    cur.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", data)

    conn.commit()
    conn.close()
    print("Done seeding.")


# OFFSET PAGINATION
@app.route('/api/v1/books', methods=["GET"])
def get_books():
    start_time = time.time()

    pagination_type = request.args.get('pagination', 'offset')

    if pagination_type == "offset":
        limit = int(request.args.get('limit', 10))
        offset = int(request.args.get('offset', 0))

        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM books ORDER BY id LIMIT ? OFFSET ?",
            (limit, offset)
        )

        rows = cur.fetchall()
        conn.close()

        duration = time.time() - start_time

        return jsonify({
            "type": "offset",
            "limit": limit,
            "offset": offset,
            "time": duration,
            "data": [dict(r) for r in rows]
        })
    
    elif pagination_type == "cursor":
        limit = int(request.args.get('limit', 10))
        last_id = request.args.get('last_id')

        conn = get_db()
        cur = conn.cursor()

        if last_id:
            cur.execute(
                "SELECT * FROM books WHERE id > ? ORDER BY id LIMIT ?",
                (int(last_id), limit)
            )
        else:
            cur.execute(
                "SELECT * FROM books ORDER BY id LIMIT ?",
                (limit,)
            )

        rows = cur.fetchall()
        conn.close()

        next_cursor = rows[-1]["id"] if rows else None
        duration = time.time() - start_time

        return jsonify({
            "type": "cursor",
            "limit": limit,
            "next_cursor": next_cursor,
            "time": duration,
            "data": [dict(r) for r in rows]
        })


@app.route('/')
def home():
    return {
        "message": "Book API with Pagination",
        "offset_example": "/api/v1/books?limit=10&offset=900000&pagination=offset",
        "cursor_example": "/api/v1/books?limit=10&last_id=900000&pagination=cursor"
    }

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=8080)
