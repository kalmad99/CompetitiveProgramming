#Using Lists
class Queue():
    def __init__(self):
        self.size = 0
        self.q1 = []

    def enqueue(self, val):
        # self.q1.append(val)
        self.q1.insert(0, val)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.q1.pop()
            # self.q1[::-1].pop()
            # return self.q1

    def size(self):
        return self.size

    def front(self):
        if self.size == 0:
            return
        else:
            return self.q1[-1]
            # return self.q1[0]

    def rear(self):
        if self.size == 0:
            return
        else:
            # return self.q1[-1]
            return self.q1[0]

    def printQueue(self):
        que = []
        for i in range(self.size):
            que.append(self.q1[i])
        print(que)

    def isEmpty(self):
        return self.size == 0


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1.enqueue(x)
        while not self.q2.isEmpty():
            self.q1.enqueue(self.q2.dequeue())

    def pop(self) -> int:
        return self.q1.dequeue()

    def top(self) -> int:
        return self.q1.front()

    def empty(self) -> bool:
        return self.q1.isEmpty()

# Using LinkedList
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.head = Node(None)
#         self.tail = self.head

#     def addTail(self, val):
#         newNode = Node(val)
#         self.tail.next = newNode
#         self.tail = self.tail.next

#     def deleteHead(self):
#         if self.empty():
#             return
#         temp = self.head.next
#         self.head.next = self.head.next.next

#         if self.empty():
#             self.tail = self.head

#         return temp.val

#     def top(self):
#         return self.tail.val
#     def empty(self):
#         return self.head.next is None

# class MyStack:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.s1 = deque()
#         self.s2 = deque()


#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.s1.append(x)

#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         temp = None
#         if self.s2.empty():

#             while(True):
#                 t = self.s1.deleteHead()
#                 if self.s1.empty():
#                     temp = t
#                     break
#                 self.s2.addTail(t)

#             while(not self.s2.empty()):
#                 self.s1.addTail(self.s2.deleteHead())
#         return temp


#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.s1.top()

#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return self.s1.empty()

s1 = MyStack()
s1.push(1)
s1.push(2)
print(s1.top())
print(s1.pop())
print(s1.empty())

