from openapi_server.db import SessionLocal
from openapi_server.models.db.product_model import Product
from flask import request, jsonify

def create_product():
    db = SessionLocal()
    data = request.json

    product = Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)

    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description
    }), 201


def get_products():
    db = SessionLocal()
    products = db.query(Product).all()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description
        })

    return jsonify(result)


def get_product_by_id(id_):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == id_).first()

    if not product:
        return {"message": "Not found"}, 404

    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description
    }


def update_product(id_):
    db = SessionLocal()
    data = request.json

    product = db.query(Product).filter(Product.id == id_).first()

    if not product:
        return {"message": "Not found"}, 404

    for key, value in data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description
    }


def delete_product(id_):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == id_).first()

    if not product:
        return {"message": "Not found"}, 404

    db.delete(product)
    db.commit()

    return {"message": "Deleted successfully"}