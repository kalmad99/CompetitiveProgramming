class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # iterative
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next and curr.next.next:
            first, second = curr.next, curr.next.next
            first.next = second.next
            curr.next = second
            second.next = first
            curr = curr.next.next

        return dummy.next