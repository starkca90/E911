from io import StringIO

import connexion
import pandas
import requests

import six

from swagger_server import util


def spreadsheet_geocode(body):  # noqa: E501
    """Populate latitude and longitude field in spreadsheet

    Populate latitude and longitude fields in all entries in uploaded spreadsheet # noqa: E501

    :param body: E911 Spreadsheet
    :type body: dict | bytes

    :rtype: str
    """
    erls = pandas.read_csv(StringIO(str(body, 'utf-8')))

    for erl in erls.loc:
        print(erl)

        nena_body = {
            "house_number": erl["HouseNumber"],
            "house_number_suffix": erl["HouseNumberSuffix"],
            "street_name": erl["StreetName"],
            "prefix_directional": erl["Prefix Directional"],
            "street_suffix": erl["Street Suffix"],
            "post_directional": erl["Post Directional"],
            "community_name": erl["Community Name"],
            "state": erl["State"],
            "zip_code": erl["ZIP Code"]
        }

    return 'do some magic!'
