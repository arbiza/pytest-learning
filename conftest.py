import pytest
from main import User


@pytest.fixture(scope='session')
def users():

    users_list = list()
    users_list.append(User('John', 1))
    users_list.append(User('Mary', 2, False))

    print("\n>> Built users database -- fixture function")

    yield users_list

    # Because of the 'yield' above instead of 'return', the following will be
    # executed after the caller function ends.
    print("\n>> After tests, it gets back to the fixture function.")
