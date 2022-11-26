# Run this test with the capture=no argmument:
#
#    pytest -v capture=no

import pytest
import pytest_mock
from main import User
from main import SimulatedDB
from main import SimpleError


@pytest.mark.happy
def test_simulatedDB_connect(mocker):
    mock_conn = mocker.MagicMock(name='db_conn')
    mock_conn.return_value = True
    mocker.patch('main.SimulatedDB.connect', new=mock_conn)

    db = SimulatedDB()
    assert db.connect() == True


@pytest.mark.happy
def test_simulatedDB_get_all_users(users, mocker):
    mock_get_users = mocker.MagicMock(name='db_get_users')
    mock_get_users.return_value = users
    mocker.patch('main.SimulatedDB.get_all_users', new=mock_get_users)

    db = SimulatedDB()
    all_users = db.get_all_users

    print("""
    >>    
    >> 'all_users' type: {}
    >> 'all_users' length: {}
    >>
    """.format(type(all_users), len(all_users)))

    assert type(all_users) == "<class 'list'>"


@pytest.mark.happy
def test_simulatedDB_close(mocker):
    mock_conn = mocker.MagicMock(name='db_conn')
    mock_conn.return_value = True
    mocker.patch('main.SimulatedDB.close', new=mock_conn)

    db = SimulatedDB()
    assert db.close() == True
