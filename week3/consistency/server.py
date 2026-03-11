from flask import Flask, jsonify

app = Flask(__name__)

mock_users = [
  { "id": 1, "name": "John" },
  { "id": 2, "name": "Claire" }
]

mock_products = [
  { "id": 101, "name": "Laptop" },
  { "id": 102, "name": "Phone" }
]

# Non-consistency examples
@app.route("/getUsers", methods=["GET"])
def get_users():
    return jsonify({"data": mock_users})

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify({"data": mock_products})

# Consistency examples
@app.route("/api/v1/users", methods=["GET"])
def get_users_v2():
    return jsonify({"data": mock_users})

@app.route("/api/v1/orders", methods=["GET"])
def get_orders_v2():
    return jsonify({"data": mock_products})

if __name__ == "__main__":
    app.run(debug=True)