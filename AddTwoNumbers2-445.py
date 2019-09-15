# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(head:ListNode):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
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
                