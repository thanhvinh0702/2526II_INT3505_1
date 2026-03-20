# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book_details import BookDetails  # noqa: E501
from swagger_server.models.book_list_response import BookListResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBooksController(BaseTestCase):
    """BooksController integration test stubs"""

    def test_create_book(self):
        """Test case for create_book

        Create a book resource
        """
        body = None
        response = self.client.open(
            '/books',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_book_by_id(self):
        """Test case for delete_book_by_id

        Delete Book by Id
        """
        response = self.client.open(
            '/books/{bookId}'.format(book_id='book_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book_by_id(self):
        """Test case for get_book_by_id

        Get Book by Id
        """
        response = self.client.open(
            '/books/{bookId}'.format(book_id='book_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_books(self):
        """Test case for list_books

        Get list of books
        """
        query_string = [('title', 'title_example'),
                        ('author', 'author_example')]
        response = self.client.open(
            '/books',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_book_by_id(self):
        """Test case for update_book_by_id

        Update Book by Id
        """
        body = None
        response = self.client.open(
            '/books/{bookId}'.format(book_id='book_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
