class Node:
    def __init__(self, data):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        length = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            length += 1
        return length

    def insert_front(self, value):
        if value is None:
            return None
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_tail(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    def find(self, data):
        if data is None:
            return None
        curr = self.head
        while curr.next is not None:
            if curr.data == data:
                return curr
        return None

    def delete(self, data):
        if data is None or self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.data == data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def delete2(self, data):
        if data is None or self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next is not None:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next
