class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(level_order):
    if not level_order or level_order[0] == "null": return None
    root = BSTNode(int(level_order[0]))
    queue = [root]
    idx = 1
    while queue and idx < len(level_order):
        node = queue.pop(0)
        if idx < len(level_order) and level_order[idx] != "null":
            node.left = BSTNode(int(level_order[idx]))
            queue.append(node.left)
        idx += 1
        if idx < len(level_order) and level_order[idx] != "null":
            node.right = BSTNode(int(level_order[idx]))
            queue.append(node.right)
        idx += 1
    return root

def is_valid_BST(node, low = -10**9, high = 10**9):
    if not node: return True
    if not (low < node.val < high): return False
    return is_valid_BST(node.left, low, node.val) and is_valid_BST(node.right, node.val, high)

if __name__ == '__main__':
    level_order = input().split() # 5 3 8 2 4 7 9 (Yes)
    root = build_tree(level_order)
    if is_valid_BST(root): print("Yes")
    else: print("No")