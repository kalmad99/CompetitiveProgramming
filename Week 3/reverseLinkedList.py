class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.ans = None

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        self.reverseAnswer(head)
        return self.ans

    def reverseAnswer(self, head):
        if head.next is None:
            self.ans = head
            return head
        else:
            res = self.reverseAnswer(head.next)
            head.next = None
            res.next = head
            return head