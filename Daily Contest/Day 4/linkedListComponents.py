# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, G) -> int:
        hashmap = set(G)
        temp = head
        counter = 0
        while temp.next:
            if temp.val in hashmap and temp.next.val not in hashmap:
                counter += 1
            temp = temp.next
        if temp.val in hashmap:
            counter += 1
        return counter