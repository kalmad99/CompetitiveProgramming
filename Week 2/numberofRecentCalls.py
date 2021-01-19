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

    def size(self):
        return self.size

    def front(self):
        if self.size == 0:
            return
        else:
            return self.q1[-1]

    def rear(self):
        if self.size == 0:
            return
        else:
            # return self.q1[-1]
            return self.q1[0]
    def printlist(self):
        for i in range(self.size):
            print(self.q1[::-1][i])

    def isEmpty(self):
        return self.size == 0


class RecentCounter:
    def __init__(self):
        self.counter = 0
        self.q = Queue()

    def ping(self, t: int) -> int:
        self.q.enqueue(t)
        while self.q.front() < t-3000:
            self.q.dequeue()
        return self.q.size


# rc = RecentCounter()
# print(rc.ping(1))
# print(rc.ping(100))
# print(rc.ping(3001))
# print(rc.ping(3002))

