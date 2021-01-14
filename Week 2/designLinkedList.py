class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # def length(self):
    #     cur = self.head
    #     count = 0
    #     while cur:
    #         cur = cur.next
    #         count+=1
    #     return count

    def addAtHead(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        cur = self.head
        new_node.next = cur
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index == 0:
            return self.addAtHead(val)
        elif index > self.size or index < 0:
            return
        else:
            curr = self.head
            prev = None
            new_node = Node(val)
            counter = 0
            while counter < index:
                prev = curr
                curr = curr.next
                counter += 1
            new_node.next = curr
            prev.next = new_node
            # for _ in range(index-1):
            #     curr = curr.next
            # new_node.next = curr.next
            # curr.next = new_node
            self.size += 1
        # self.printer()

    def deleteAtIndex(self, index: int) -> None:
        if self.size == 1 and index == 0:
            self.head = None
            self.size -= 1
            return
        elif self.size == index + 1:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None

        elif index == 0:
            self.head = self.head.next

        elif index + 1 > self.size or index < 0:
            return
        else:
            curr = self.head
            fast = self.head.next
            for _ in range(index - 1):
                curr = fast
                fast = fast.next
            curr.next = fast.next
        self.size -= 1

    def get(self, index):
        cur = self.head
        counter = 0
        if index < 0 or index >= self.size:
            return -1
        while counter < index and cur:
            cur = cur.next
            counter += 1
        if cur is None:
            return
        else:
            return cur.val

# def addAtIndex(self, val, index):
    #     new_node = Node(val)
    #     if self.head is None:
    #         self.head = new_node
    #         self.size += 1
    #         return
    #     else:
    #         cur = self.head
    #         counter = 1
    #         prev = None
    #         while cur and counter < index:
    #             prev = cur
    #             cur = cur.next
    #         if cur is None:
    #             return
    #         else:
    #             prev.next = new_node
    #             new_node.next = cur
    #         self.size += 1
    #
    # def deleteAtIndex(self, index):
    #     if index < 0 or index > self.size - 1:
    #         return -1
    #     elif index == 0 and self.size == 1:
    #         self.head = None
    #         self.size -= 1
    #     elif index == 0 and self.size > 1:
    #         cur = self.head
    #         self.head = cur.next
    #         cur = None
    #         self.size -= 1
    #     else:
    #         cur = self.head
    #         counter = 1
    #         prev = None
    #         while counter < index and cur:
    #             prev = cur
    #             cur = cur.next
    #             counter += 1
    #         if cur is None:
    #             return
    #         else:
    #             prev.next = cur.next
    #             cur = None
    #         self.size -= 1
