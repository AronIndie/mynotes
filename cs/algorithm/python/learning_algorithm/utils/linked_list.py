class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def gen_linked_list(n):
    init = Node(0)
    temp = init
    for i in range(1, n):
        temp.next = Node(i)
        temp = temp.next
    return init

def display(head):
    while head is not None:
        print(head.value)
        head = head.next