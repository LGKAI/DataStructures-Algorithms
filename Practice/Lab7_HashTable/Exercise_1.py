class HashNode:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value

class DeletedNode: # đánh dấu phần tử bị xoá (lazy deletion)
    pass

DELETED = DeletedNode()

class HashTable:
    def __init__(self, hashSize: int) -> None:
        self.capacity = hashSize
        self.table = [None] * self.capacity

    def __del__(self) -> None:
        print("HashTable deleted.")

    def _hash(self, key: str, i: int) -> int:
        return (hash(key) + i) % self.capacity

    def add(self, key: str, value: int) -> None:
        first_deleted_index = -1
        for i in range(self.capacity):
            index = self._hash(key, i)
            if self.table[index] is None:
                if first_deleted_index != -1:
                    index = first_deleted_index
                self.table[index] = HashNode(key, value)
                return
            elif isinstance(self.table[index], DeletedNode):
                if first_deleted_index == -1:
                    first_deleted_index = index
            elif self.table[index].key == key:
                self.table[index].value = value
                return
        print("HashTable is full! Cannot insert key:", key)

    def searchValue(self, key: str) -> int:
        for i in range(self.capacity):
            index = self._hash(key, i)
            if self.table[index] is None:
                return None
            elif isinstance(self.table[index], HashNode) and self.table[index].key == key:
                return self.table[index].value
        return None

    def removeKey(self, key: str) -> None:
        for i in range(self.capacity):
            index = self._hash(key, i)
            if self.table[index] is None:
                return
            elif isinstance(self.table[index], HashNode) and self.table[index].key == key:
                self.table[index] = DELETED # lazy deletion
                return


if __name__ == "__main__":
    ht = HashTable(10)
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
