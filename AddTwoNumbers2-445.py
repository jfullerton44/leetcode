# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head:ListNode) -> ListNode:
            prev = None
            curr = None
            while head:
                curr = head.next
                head.next = prev
                prev = head
                head = curr
            return prev

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        print(l1.val)
        print(l2.val)
        val, carry = 0,0
        head = ListNode(-1)
        cur = head
        while l1 or l2:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val +=l2.val
                l2 = l2.next
            val+=carry
            cur.next = ListNode((val)%10)
            cur = cur.next
            carry = int(val/10)
            val = 0
        if(carry!=0):
            cur.next = ListNode(carry)
        return reverseList(head.next)
                