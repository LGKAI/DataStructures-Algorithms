class HashNode:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None # dùng để liên kết các node trong cùng 1 bucket

class HashTable:
    def __init__(self, hashSize: int) -> None:
        self.capacity = hashSize
        self.table = [None] * self.capacity

    def __del__(self) -> None:
        print("HashTable deleted.")

    def _hash(self, key: str) -> int:
        return hash(key) % self.capacity

    def add(self, key: str, value: int) -> None:
        index = self._hash(key)
        head = self.table[index]
        # Kiểm tra nếu key đã tồn tại -> cập nhật
        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        # Nếu không tìm thấy, chèn node mới vào đầu danh sách
        new_node = HashNode(key, value)
        new_node.next = head
        self.table[index] = new_node

    def searchValue(self, key: str) -> int:
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def removeKey(self, key: str) -> None:
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next


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
