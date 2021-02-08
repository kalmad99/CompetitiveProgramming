import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        minheap = self.nums
        heapq.heapify(minheap)
        heapq.heappush(minheap, val)
        while len(minheap) > self.k:
            heapq.heappop(minheap)
        return minheap[0]

