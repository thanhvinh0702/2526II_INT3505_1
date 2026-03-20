import connexion
import six

from swagger_server.models.book_details import BookDetails  # noqa: E501
from swagger_server.models.book_list_response import BookListResponse  # noqa: E501
from swagger_server import util


def create_book(body):  # noqa: E501
    """Create a book resource

     # noqa: E501

    :param body: Body to create/put book resource
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_book_by_id(book_id):  # noqa: E501
    """Delete Book by Id

     # noqa: E501

    :param book_id: The unique identifier of a book
    :type book_id: str

    :rtype: BookDetails
    """
    return 'do some magic!'


def get_book_by_id(book_id):  # noqa: E501
    """Get Book by Id

     # noqa: E501

    :param book_id: The unique identifier of a book
    :type book_id: str

    :rtype: BookDetails
    """
    return 'do some magic!'


def list_books(title=None, author=None):  # noqa: E501
    """Get list of books

     # noqa: E501

    :param title: A query string use for filtering book by title
    :type title: str
    :param author: A query string use for filtering book by author
    :type author: str

    :rtype: BookListResponse
    """
    return 'do some magic!'


def update_book_by_id(body, book_id):  # noqa: E501
    """Update Book by Id

     # noqa: E501

    :param body: Body to create/put book resource
    :type body: dict | bytes
    :param book_id: The unique identifier of a book
    :type book_id: str

    :rtype: BookDetails
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
