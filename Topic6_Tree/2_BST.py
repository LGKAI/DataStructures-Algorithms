class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Trường hợp node có 1 con hoặc không có con
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Trường hợp node có 2 con
            # Tìm phần tử nhỏ nhất ở cây con bên phải để thay thế
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Duyệt cây theo thứ tự in-order để in ra các phần tử
    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


if __name__ == "__main__":
    bst = BST()

    # Kiểm tra cây rỗng
    print("Cây có rỗng không?", bst.is_empty())

    # Thêm phần tử vào cây
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # Duyệt cây in-order
    print("Cây sau khi thêm các phần tử:", bst.inorder_traversal())

    # Tìm phần tử
    print("Tìm 40 trong cây:", bst.find(40))
    print("Tìm 90 trong cây:", bst.find(90))

    # Xóa 1 phần tử
    bst.delete(30)
    print("Cây sau khi xóa 30:", bst.inorder_traversal())
    bst.delete(50)
    print("Cây sau khi xóa 50:", bst.inorder_traversal())