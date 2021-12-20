class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.heigth = 1

    def print_stack(self):
        temp = self.top

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.heigth == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.heigth += 1

    def pop(self):
        if self.heigth == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.heigth -= 1
        return temp


my_stack = Stack(2)
my_stack.push(1)
my_stack.push(0)
my_stack.pop()
my_stack.print_stack()
