# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestSpreadsheetController(BaseTestCase):
    """SpreadsheetController integration test stubs"""

    def test_spreadsheet_geocode(self):
        """Test case for spreadsheet_geocode

        Populate latitude and longitude field in spreadsheet
        """
        body = Object()
        response = self.client.open(
            '/spreadsheet/geocode/',
            method='POST',
            data=json.dumps(body),
            content_type='text/csv')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
