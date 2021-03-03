import requests
import pytest
import json

""" This module runs a sequence of related REST API tests using the Requests library
The Request class has these params:
method=None, url=None, headers=None, files=None, data=None,
params=None, auth=None, cookies=None, hooks=None, json=None
"""

BASE_URL = ''
BEARER_TOKEN = ''

car = ''
person = ''

vfn_id = None
'''In PyTest, a class cannot have an __init__ method because PyTest needs to use that.
For sequences of tests(ie. integration tests) share between test methods using fixtures.'''


def test_welcome():
    """ This GET request to the welcome url should return a 200 and tests access.

    """
    request_url = BASE_URL + '/api/v1/people'
    resp = requests.get(
        request_url,
        headers={'Accept': 'application/json',
                 'Token': BEARER_TOKEN
                 }
    )
    assert resp.status_code == 200
