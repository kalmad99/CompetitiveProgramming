# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Reverse:
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


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        r = Reverse()
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        fast = head
        slow = r.reverseList(slow)

        while slow is not None:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next

        return True

