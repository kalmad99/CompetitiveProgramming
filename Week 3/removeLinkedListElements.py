# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = head
        prev = None
        if head is None:
            return
        while temp.next is not None:
            if temp.val == val:
                temp.val = temp.next.val
                temp.next = temp.next.next
            else:
                prev = temp
                temp = temp.next
        if prev is None and temp.val == val:
            return None
        if temp.val == val:
            prev.next = None
        return head