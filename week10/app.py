from flask import Flask, jsonify, request, make_response
from datetime import datetime

app = Flask(__name__)

V1_DEPRECATION_DATE = "2026-08-01"
V1_SUNSET_DATE = "2026-12-01"

def add_deprecation_headers(response):
    response.headers["Deprecation"] = "true"

    response.headers["Sunset"] = V1_SUNSET_DATE

    response.headers["Link"] = (
        '</api/docs/v2-migration>; '
        'rel="deprecation"; '
        'type="text/html"'
    )

    response.headers["Warning"] = (
        '299 - "API v1 is deprecated. '
        'Please migrate to API v2 before 2026-12-01"'
    )

    return response

@app.route("/api/v1/payment", methods=["POST"])
def payment_v1():

    data = request.json

    response = make_response(jsonify({
        "version": "v1",
        "status": "success",
        "message": "Payment processed",

        "deprecated": True,

        "deprecation_notice": {
            "deprecated_since": V1_DEPRECATION_DATE,
            "sunset_date": V1_SUNSET_DATE,
            "migration_guide": "/api/docs/v2-migration"
        }
    }))

    response = add_deprecation_headers(response)

    return response

@app.route("/api/v2/payment", methods=["POST"])
def payment_v2():

    data = request.json

    return jsonify({
        "version": "v2",
        "status": "success",
        "transaction_id": "TXN-123456",
        "processed_at": datetime.utcnow().isoformat(),
        "message": "Payment processed successfully"
    })

@app.route("/api/docs/v2-migration")
def migration_guide():

    return jsonify({
        "title": "Migration Guide v1 -> v2",

        "changes": [
            {
                "field": "amount",
                "change": "must be integer instead of string"
            },
            {
                "field": "currency",
                "change": "required in v2"
            },
            {
                "field": "transaction_id",
                "change": "new response field"
            }
        ],

        "example_v2_request": {
            "amount": 1000,
            "currency": "USD"
        }
    })


if __name__ == "__main__":
    app.run(debug=True)