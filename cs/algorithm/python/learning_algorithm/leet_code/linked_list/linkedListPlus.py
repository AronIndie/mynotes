
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def find_node(node, i):
    count = 0
    while count < i:
        node = node.next
        if node == None:
            break
        count +=1
    return node


class Solution:
    def get_node(self, node, i):
        count = 0
        while count < i:
            node = node.next
            if node == None:
                raise Exception("index out of bound")
            count += 1
        return node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None
        length = 0
        s2 = 0
        while l1 != None and l2 != None:
            if l1 == None:
                s1 = l2.val
                s2 = 0
            elif l2 == None:
                s1 = l1.val
                s2 = 0
            else:
                s = l1.val + l2.val + s2
                s1 = s % 10
                s2 = s // 10

            if length == 0:
                res = ListNode(s1)
            else:
                pre_node = self.get_node(res, length - 1)
                pre_node.next = ListNode(s1)
            length += 1
            l1 = l1.next
            l2 = l2.next

        return res

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    a = Solution()
    a.addTwoNumbers(l1, l2)