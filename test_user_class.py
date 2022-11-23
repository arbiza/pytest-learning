import pytest
from main import User
from main import SimpleError


@pytest.mark.happy
def test_user_create():

    users = []

    users.append(User('John', 1, True))
    users.append(User('Mary', 2, False))

    assert users[0].name == 'John'
    assert users[0].id == 1
    assert users[0].status == 'Active'

    assert users[1].name == 'Mary'
    assert users[1].id == 2
    assert users[1].status == 'Inactive'


@pytest.mark.happy
def test_user_create_minimun_args():
    user = User('John', 1)

    assert user.name == 'John'
    assert user.id == 1
    assert user.status == 'Active'


@pytest.mark.sad
def test_user_create_missing_args():
    with pytest.raises(TypeError) as exp:
        user = User()
    assert "__init__() missing 2 required positional arguments: 'name' and 'id'" in str(exp.value)


@pytest.mark.sad
def test_user_change_name():
    user = User('John', 1)
    with pytest.raises(SimpleError) as exp:
        user.name = 'Marcus'
        pass
    assert str(exp.value) == "The 'name' attribute can't be set/changed directly"


@pytest.mark.sad
def test_user_change_id():
    user = User('John', 1)
    with pytest.raises(SimpleError) as exp:
        user.id = 10
        pass
    assert str(exp.value) == "The 'id' attribute can't be set/changed directly"


@pytest.mark.sad
def test_user_change_status():
    user = User('John', 1)
    with pytest.raises(SimpleError) as exp:
        user.status = 'Inactive'
        pass
    assert str(exp.value) == "The 'status' attribute can't be set/changed directly"
