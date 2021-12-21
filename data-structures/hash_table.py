from _typeshed import IdentityFunction


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] * size]

    def _hash(self, key):
        return key % self.size

    def set(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item.key == key:
                item.value = value
                return
        self.table[index].append(Item(key, value))

    def get(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item.key == key:
                del self.table[index][i]
                return
        raise KeyError('Key not found')
