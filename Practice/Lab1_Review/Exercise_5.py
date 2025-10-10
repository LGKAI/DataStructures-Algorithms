from Exercise_4 import LinkedList

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, data):
        self.linked_list.add_head(data)

    def pop(self):
        if not self.linked_list.head:
            print("Stack is empty!")
            return None
        top_data = self.linked_list.head.data
        self.linked_list.remove_head()
        return top_data

    def top(self):
        if not self.linked_list.head:
            print("Stack is empty!")
            return None
        return self.linked_list.head.data
    

if __name__ == '__main__':
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top item:", stack.top()) # 30
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Top item again:", stack.top()) # 10

