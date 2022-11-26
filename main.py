import time


class SimpleError(Exception):
    pass


class User():
    def __init__(self, name, id, active=True):

        self._name = name
        self._id = id
        self._status = active

    # The following methods ensure the attributes are private and can't be
    # set/changed directly.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        raise SimpleError("The 'name' attribute can't be set/changed directly")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        raise SimpleError("The 'id' attribute can't be set/changed directly")

    @property
    def status(self):
        return 'Active' if self._status else 'Inactive'

    @status.setter
    def status(self, status):
        raise SimpleError(
            "The 'status' attribute can't be set/changed directly")

    # Defines how the object will be printed with 'print()'
    def __str__(self):
        return "Name: {}\n"\
            "  ID: {}\n"\
            "  Status: {}\n\n".format(self._name, self._id,
                                      'Active' if self._status else 'Inactive')


class SimulatedDB():
    def __init__(self):
        self._users = list()
        self._conn = False

    def connect(self):
        time.sleep(4)
        self._conn = True
        return True

    def get_all_users(self):
        if self._conn:
            time.sleep(10)
            self._users.append(User('John', 1))
            self._users.append(User('Mary', 2, False))
            return self._users
        else:
            time.sleep(3)
            raise SimpleError("There is no active connection to the DB")

    def close(self):
        if self._conn:
            self._conn = False
            time.sleep(3)
            return True
        else:
            time.sleep(3)
            raise SimpleError("There is no active connection to the DB")


if __name__ == "__main__":

    db = SimulatedDB()
    db.connect()
    users = db.get_all_users()
    db.close()

    for user in users:
        print(user)
