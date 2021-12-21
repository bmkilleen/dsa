class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None and self.tail is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        self.head = self.head.next
        return data
