from Exercise_4 import LinkedList

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, data):
        self.linked_list.add_tail(data)

    def dequeue(self):
        if not self.linked_list.head:
            print("Queue is empty!")
            return None
        front_data = self.linked_list.head.data
        self.linked_list.remove_head()
        return front_data

    def front(self):
        if not self.linked_list.head:
            print("Queue is empty!")
            return None
        return self.linked_list.head.data


if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Front item:", queue.front()) # 10
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Front item again:", queue.front()) # 30
