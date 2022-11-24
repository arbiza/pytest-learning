import pytest
from main import User
from main import SimulatedDB


@pytest.fixture(scope='session')
def users():

    db = SimulatedDB()
    db.connect()
    users = db.get_all_users()

    print("\n>> Built users database -- fixture function")

    yield users

    # Because of the 'yield' above instead of 'return', the following will be
    # executed after the caller function ends.
    print("\n>> After tests, it gets back to the fixture function.")
    db.close()
