from functools import reduce


class Friends:
    def __init__(self, connections):
        self._connections = list(connections)

    def add(self, connection):
        if connection in self._connections:
            return False

        self._connections.append(connection)
        return True

    def remove(self, connection):
        if connection not in self._connections:
            return False

        self._connections.remove(connection)
        return True

    def names(self):
        all_names = reduce(lambda x, y: x | y, self._connections, set())
        return set(all_names)

    def connected(self, name):
        friends = set()
        for connection in self._connections:
            if name in connection:
                friends |= connection - {name}
        return friends

    def __repr__(self):
        return f'Friends(connections={self._connections})'


friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))

assert friends.connected("a") == {"b", "c"}
assert friends.connected("d") == set()
assert friends.remove({"c", "a"}) is True
assert friends.connected("c") == {'b'}

print(friends)

