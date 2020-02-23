import pytest

import keysafe
from keysafe.tests import *
from keysafe.src.safe import safe

def init_secure():

    x = safe(safe.CREDS_TYPE_SECURE)
    x.service = service
    x.alias = alias
    x.user = user
    x.password = password
    return x

def init_unsecure():

    y = safe(safe.CREDS_TYPE_PLAIN)
    y.alias =  alias
    y.plain.location = dir_data
    return y

def test_create_and_verify_secure():

    x = init_secure()
    y = init_secure()
    x.set()
    y.get()
    assert y.password == password

def test_create_and_modify_secure():

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

def test_credentials_unsecure_valid():

    x = init_unsecure()
    x.get()
    assert x.user == user
    assert x.password == password
