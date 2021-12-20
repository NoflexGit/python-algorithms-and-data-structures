class Node:
    def __init__(self, value):
        self.value = value
        self.value = None


class Queue:
    def __init__(self, value):
        self.first = Node(value)
        self.last = Node(value)
        self.length = 1

    def print_queue(self):
        temp = self.first.next

        while temp is not None:
            print(temp.value)
            temp = temp.next
