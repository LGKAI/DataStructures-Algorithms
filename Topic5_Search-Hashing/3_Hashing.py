class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = self.hash(key)
        return key in self.table[index]

    def __str__(self):
        return str(self.table)

class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        start_index = index
        while self.table[index] is not None and self.table[index] != key:
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash table is full")
        self.table[index] = key

    def search(self, key):
        index = self.hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
            if index == start_index:
                break
        return False

    def __str__(self):
        return str(self.table)
    

if __name__ == '__main__':
    pass
