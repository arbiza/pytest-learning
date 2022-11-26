# Run this test with the capture=no argmument:
#
#    pytest -v capture=no

import pytest
from main import User
from main import SimpleError


@pytest.mark.happy
@pytest.mark.parametrize("index,attr,expected", [
    (0, 'name', 'John'),
    (0, 'id', 1),
    (0, 'status', 'Active'),
    (1, 'name', 'Mary'),
    (1, 'id', 2),
    (1, 'status', 'Inactive')
])
def test_user_create(users, index, attr, expected):
    # The data passed with
    assert getattr(users[index], attr) == expected
