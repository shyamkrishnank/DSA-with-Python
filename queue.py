class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class queue:
    def __init__(self):
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = temp.next
        temp.next = None
        return temp

    def print_queue(self):
        if self.length == 0:
            return None
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
