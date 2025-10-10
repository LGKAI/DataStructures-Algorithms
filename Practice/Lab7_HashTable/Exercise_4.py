class HashNode:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 # cần cho AVL balance

# AVL functions
def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def insert_avl(root, key, value):
    if not root:
        return HashNode(key, value)

    if key < root.key:
        root.left = insert_avl(root.left, key, value)
    elif key > root.key:
        root.right = insert_avl(root.right, key, value)
    else:
        root.value = value
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Left Left
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right Right
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left Right
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def search_avl(root, key):
    if not root:
        return None
    if key == root.key:
        return root.value
    elif key < root.key:
        return search_avl(root.left, key)
    else:
        return search_avl(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete_avl(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_avl(root.left, key)
    elif key > root.key:
        root.right = delete_avl(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = min_value_node(root.right)
        root.key = temp.key
        root.value = temp.value
        root.right = delete_avl(root.right, temp.key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Balance cases
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)

    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)

    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Hash table with AVL chaining
class HashTable:
    def __init__(self, hashSize: int) -> None:
        self.capacity = hashSize
        self.table = [None] * self.capacity

    def _hash(self, key: str) -> int:
        return hash(key) % self.capacity

    def add(self, key: str, value: int) -> None:
        index = self._hash(key)
        self.table[index] = insert_avl(self.table[index], key, value)

    def searchValue(self, key: str) -> int:
        index = self._hash(key)
        return search_avl(self.table[index], key)

    def removeKey(self, key: str) -> None:
        index = self._hash(key)
        self.table[index] = delete_avl(self.table[index], key)


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
