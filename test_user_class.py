# Run this test with the capture=no argmument:
#
#    pytest --capture=no

import pytest
from main import User
from main import SimpleError


@pytest.fixture(scope='module')
def users():

    users_list = list()
    users_list.append(User('John', 1))
    users_list.append(User('Mary', 2, False))

    print("\n>> Built users database -- fixture function")

    yield users_list

    # Because of the 'yield' above instead of 'return', the following will be
    # executed after the caller function ends.
    print("\n>> After tests, it gets back to the fixture function.")


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
