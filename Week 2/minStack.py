class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.mini = [2**31-1]
        self.counter = 0

    def push(self, x: int) -> None:
        self.s1.append(x)
        if x <= self.mini[self.counter]:
            self.mini.append(x)
            self.counter+=1
        # print(self.mini)

    def pop(self) -> None:
        if self.s1[len(self.s1)-1] == self.mini[-1]:
            self.mini.pop()
            self.counter -=1
        self.s1.pop()

    def top(self) -> int:
        return self.s1[len(self.s1)-1]

    def getMin(self) -> int:
        return self.mini[-1]

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())
# minStack.pop()
# print(minStack.top())
# print(minStack.getMin())

# minStack = MinStack()
# print(minStack.push(2147483646))
# print(minStack.push(2147483646))
# print(minStack.push(2147483647))
# print(minStack.top())
# print(minStack.pop())
# print(minStack.getMin())
# print(minStack.pop())
# print(minStack.getMin())
# print(minStack.pop())
# print(minStack.push(2147483647))
# print(minStack.top())
# print(minStack.getMin())
# print(minStack.push(-2147483648))
# print(minStack.top())
# print(minStack.getMin())
# print(minStack.pop())
# print(minStack.getMin())
