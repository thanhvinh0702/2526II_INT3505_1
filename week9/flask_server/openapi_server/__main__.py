#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from openapi_server.db import engine
from openapi_server.models.db.product_model import Product


def main():
    Product.metadata.create_all(bind=engine)
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Product API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
