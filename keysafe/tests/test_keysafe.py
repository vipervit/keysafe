import pytest

from keysafe import safe
from keysafe.tests import *

def init_secure():

    x = safe(safe.CREDS_TYPE_SECURE)
    x.service = service
    x.alias = alias
    x.user = user
    return x

def init_plain():

    x = safe(safe.CREDS_TYPE_PLAIN)
    x.plain.location = dir_data
    x.alias =  alias
    x.user = user
    return x

def test_set_secure():

    x = init_secure()
    y = init_secure()
    x.password = password
    x.set()
    y.get()
    assert y.password == password

def test_set_modify_secure():

    x = init_secure()
    y = init_secure()
    x.password = password
    x.set()
    x.password = newpassword
    x.set()
    y.get()
    assert y.password == newpassword


def test_delete_secure():

    x = init_secure()
    x.password = password
    x.set()
    y = init_secure()
    y.password = None
    x.delete()
    y.get()
    assert y.password is None

def test_plain_set():

    x = init_plain()
    y = init_plain()
    x.password = password
    x.set()
    y.get()
    assert y.password == password

def test_set_modify_plain():

    x = init_plain()
    y = init_plain()
    x.password = password
    x.set()
    assert x.plain.file_exists()
    y.get()
    assert y.password == password

def test_set_modify_plain():

    x = init_plain()
    y = init_plain()
    x.password = password
    x.set()
    x.password = newpassword
    x.set()
    y.get()
    assert y.password == newpassword

def test_delete_plain():
    x = init_plain()
    x.delete()
    assert not x.plain.file_exists()
