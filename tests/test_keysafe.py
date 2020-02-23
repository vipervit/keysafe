import pytest

import keysafe
from keysafe.tests import dir_data
from keysafe.src.safe import safe

test_service = 'KEYSAFE_TEST'
test_alias = 'keysafe_username'
test_user = 'keysafe_userid'
test_password = 'keysafe_password'


def init_secure():

    x = safe(safe.CREDS_TYPE_SECURE)
    x.service = test_service
    x.alias = test_alias
    x.user = test_user
    x.password = test_password
    return x

def init_unsecure():

    y = safe(safe.CREDS_TYPE_PLAIN)
    y.alias = test_alias
    y.user = test_user
    return y

def test_create_and_verify_secure():

    x = init_secure()
    y = init_secure()
    x.set()
    y.get()
    assert y.password == test_password

def test_create_and_modify_secure():

    newpassword = 'newpassword'
    x = init_secure()
    y = init_secure()
    x.set()
    x.password = newpassword
    x.set()
    y.get()
    assert y.password == newpassword


def test_delete_secure():

    x = init_secure()
    x.set()
    y = init_secure()
    y.password = None
    x.delete()
    y.get()
    assert y.password is None

# def test_credentials_unsecure_valid():
#
#     x = init_unsecure()
#     x.alias = test_alias
#     x.plain.location = dir_data
#     x.get()
#     assert x.user == test_user
#     assert x.password == test_password
