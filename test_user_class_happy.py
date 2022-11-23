# Run this test with the capture=no argmument:
#
#    pytest --capture=no

import pytest
from main import User
from main import SimpleError


@pytest.mark.happy
def test_user_create(users):

    assert users[0].name == 'John'
    assert users[0].id == 1
    assert users[0].status == 'Active'

    assert users[1].name == 'Mary'
    assert users[1].id == 2
    assert users[1].status == 'Inactive'

    print(users[-1])


@pytest.mark.happy
def test_user_create_minimun_args(users):
    assert users[0].name == 'John'
    assert users[0].id == 1
    assert users[0].status == 'Active'

    print(users[-1])


@pytest.mark.happy
def test_user_create_new_user(users):

    users.append(User('New guy', 3))
    assert len(users) == 3

    print(users[-1])
