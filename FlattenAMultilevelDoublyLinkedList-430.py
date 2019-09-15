"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        ret = head
        while(head is not None):
            if head.child is not None:
                temp = head.next
                head.next = self.flatten(head.child)
                head.child = None
                node = head.next
                node.prev = head
                while(node.next is not None):
                    node = node.next
                node.next = temp
                if temp is not None:
                    temp.prev = node
            head = head.next
        return ret
        