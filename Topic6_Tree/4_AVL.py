class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # chiều cao (ban đầu là 1)

class AVL:
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root): # tính hiệu chiều cao con trái và con phải
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, z): # quay phải
        y = z.left
        T3 = y.right
        # Thực hiện quay
        y.right = z
        z.left = T3
        # Cập nhật chiều cao
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z): # quay trái
        y = z.right
        T2 = y.left
        # Thực hiện quay
        y.left = z
        z.right = T2
        # Cập nhật chiều cao
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        # Chèn như BST
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        # Cập nhật chiều cao
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        # Kiểm tra cân bằng
        balance = self.get_balance(root)
        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node có 1 con hoặc không có con
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Node có 2 con
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        # Cập nhật chiều cao
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        # Kiểm tra cân bằng
        balance = self.get_balance(root)
        # Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        # Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        # Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    # Duyệt cây theo thứ tự in-order
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.key, end=' ')
        self.in_order(root.right)


if __name__ == '__main__':
    tree = AVL()
    root = None

    # Thêm node vào cây
    nums = [10, 20, 30, 40, 50, 25]
    for num in nums:
        root = tree.insert(root, num)

    # Duyệt cây
    print("In-order traversal of AVL tree:")
    tree.in_order(root)

    # Xoá 1 node
    print("\n\nDeleting 40...")
    root = tree.delete(root, 40)
    print("In-order traversal after deletion:")
    tree.in_order(root)