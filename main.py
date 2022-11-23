
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


if __name__ == "__main__":

    users = list()

    users.append(User('John', 1, True))
    users.append(User('Mary', 2, True))
    users.append(User('Boni', 3, False))
    users.append(User('Antonio', 4, True))
    users.append(User('Juca', 5, True))

    for user in users:
        print(user)
