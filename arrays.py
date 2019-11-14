class Array(object):
    def __init__(self, capacity, fillvalue = None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillvalue)

    def __len__(self):
        """-> The string representation of the array"""
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value

    def setvalue(self, key, value):
        self._items[key] = value

