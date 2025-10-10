class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        cur = self.head
        while cur:
            print(cur.data, end = " -> ")
            cur = cur.next
        print("None")

    def count_nodes(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def add_head(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def add_tail(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def remove_head(self):
        if not self.head:
            return
        self.head = self.head.next

    def remove_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next and cur.next.next:
            cur = cur.next
        cur.next = None

    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()
        cur = self.head
        seen.add(cur.data)
        while cur.next:
            if cur.next.data in seen:
                cur.next = cur.next.next
            else:
                seen.add(cur.next.data)
                cur = cur.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.add_tail(1)
    ll.add_tail(2)
    ll.add_tail(2)
    ll.add_tail(3)

    ll.traverse() # 1 -> 2 -> 2 -> 3 -> None
    ll.remove_duplicates()
    ll.traverse() # 1 -> 2 -> 3 -> None
    print("Node count:", ll.count_nodes()) # 3
