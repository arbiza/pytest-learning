# Run this test with the capture=no argmument:
#
#    pytest --capture=no

import pytest
from main import User
from main import SimpleError


@pytest.mark.sad
def test_user_create_missing_args(users):
    with pytest.raises(TypeError) as exp:
        user = User()
    assert "__init__() missing 2 required positional arguments: 'name' and 'id'" in str(exp.value)

    print(users[-1])


@pytest.mark.sad
def test_user_change_name(users):
    with pytest.raises(SimpleError) as exp:
        users[0].name = 'Marcus'
        pass
    assert str(exp.value) == "The 'name' attribute can't be set/changed directly"

    print(users[-1])


@pytest.mark.sad
def test_user_change_id(users):
    with pytest.raises(SimpleError) as exp:
        users[0].id = 10
        pass
    assert str(exp.value) == "The 'id' attribute can't be set/changed directly"

    print(users[-1])


@pytest.mark.sad
def test_user_change_status(users):
    with pytest.raises(SimpleError) as exp:
        users[0].status = 'Inactive'
        pass
    assert str(exp.value) == "The 'status' attribute can't be set/changed directly"

    print(users[-1])
