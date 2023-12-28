# not finished
class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def set(self, key, value):
        for idx, item in enumerate(self.data):
            if item is not None and item[0] == key:
                self.data[idx] = [key, value]
                return

        self.data.append([key, value])

    def get(self, key):
        for item in self.data:
            if item is not None and item[0] == key:
                return item[1]

        return None

    def __str__(self):
        for item in self.data:
            if item is not None:
                print(item)

        return ''
