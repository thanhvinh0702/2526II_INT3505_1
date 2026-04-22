import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.delete_response import DeleteResponse  # noqa: E501
from openapi_server.models.product import Product  # noqa: E501
from openapi_server.models.product_input import ProductInput  # noqa: E501
from openapi_server import util


def products_get():  # noqa: E501
    """Get all products

     # noqa: E501


    :rtype: Union[List[Product], Tuple[List[Product], int], Tuple[List[Product], int, Dict[str, str]]
    """
    return 'do some magic!'


def products_id_delete(id):  # noqa: E501
    """Delete product

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[DeleteResponse, Tuple[DeleteResponse, int], Tuple[DeleteResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def products_id_get(id):  # noqa: E501
    """Get product by id

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[Product, Tuple[Product, int], Tuple[Product, int, Dict[str, str]]
    """
    return 'do some magic!'


def products_id_put(id, body):  # noqa: E501
    """Update product

     # noqa: E501

    :param id: 
    :type id: str
    :param product_input: 
    :type product_input: dict | bytes

    :rtype: Union[Product, Tuple[Product, int], Tuple[Product, int, Dict[str, str]]
    """
    product_input = body
    if connexion.request.is_json:
        product_input = ProductInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def products_post(body):  # noqa: E501
    """Create product

     # noqa: E501

    :param product_input: 
    :type product_input: dict | bytes

    :rtype: Union[Product, Tuple[Product, int], Tuple[Product, int, Dict[str, str]]
    """
    product_input = body
    if connexion.request.is_json:
        product_input = ProductInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
