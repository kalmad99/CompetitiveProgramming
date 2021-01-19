class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.deque = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) < self.size:
            self.deque.append(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) < self.size:
            self.deque.insert(0, value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) > 0:
            self.deque.pop(0)
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[-1]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[0]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if len(self.deque) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.deque) == self.size:
            return True
        else:
            return False


# obj = MyCircularDeque(3)
# print(obj.insertLast(1))
# print(obj.insertLast(2))
# print(obj.insertFront(3))
# print(obj.insertFront(4))
# print(obj.getRear())
# print(obj.isFull())
# print(obj.deleteLast())
# print(obj.insertFront(4))
# print(obj.getFront())
