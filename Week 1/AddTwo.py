# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        total = 0
        dummy = ListNode(-1)
        prev = dummy
        dummy.next = prev
        while l1 != None or l2 != None:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            prev.next = ListNode((l1v + l2v + carry) % 10)
            if l1v + l2v + carry < 10:
                carry = 0
            else:
                carry = 1
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

            prev = prev.next

        if carry == 1:
            prev.next = ListNode(1)
        return dummy.next