class HashNode:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value

class DeletedNode:
    pass

DELETED = DeletedNode()

class HashTable:
    def __init__(self, capacity: int, prime: int):
        self.capacity = capacity
        self.prime = prime # số nguyên tố < capacity
        self.table = [None] * self.capacity

    def _hash1(self, key: str) -> int:
        return hash(key) % self.capacity

    def _hash2(self, key: str) -> int:
        return 1 + (hash(key) % self.prime)

    def _double_hash(self, key: str, i: int) -> int:
        return (self._hash1(key) + i * self._hash2(key)) % self.capacity

    def add(self, key: str, value: int) -> None:
        first_deleted = -1
        for i in range(self.capacity):
            index = self._double_hash(key, i)
            node = self.table[index]

            if node is None:
                if first_deleted != -1:
                    self.table[first_deleted] = HashNode(key, value)
                else:
                    self.table[index] = HashNode(key, value)
                return

            elif isinstance(node, DeletedNode):
                if first_deleted == -1:
                    first_deleted = index

            elif node.key == key:
                self.table[index].value = value # update
                return

        print("HashTable is full! Cannot insert key:", key)

    def searchValue(self, key: str) -> int:
        for i in range(self.capacity):
            index = self._double_hash(key, i)
            node = self.table[index]

            if node is None:
                return None
            elif isinstance(node, HashNode) and node.key == key:
                return node.value

        return None

    def removeKey(self, key: str) -> None:
        for i in range(self.capacity):
            index = self._double_hash(key, i)
            node = self.table[index]

            if node is None:
                return
            elif isinstance(node, HashNode) and node.key == key:
                self.table[index] = DELETED
                return


if __name__ == "__main__":
    ht = HashTable(capacity=10, prime=7)

    ht.add("apple", 10)
    ht.add("banana", 20)
    ht.add("orange", 30)

    print("Search 'apple':", ht.searchValue("apple"))
    print("Search 'banana':", ht.searchValue("banana"))
    print("Search 'grape':", ht.searchValue("grape"))

    ht.removeKey("banana")
    print("Search 'banana' after removal:", ht.searchValue("banana"))

    ht.add("grape", 40)
    print("Search 'grape':", ht.searchValue("grape"))
