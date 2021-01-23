import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        heap = []
        for key in dictionary:
            heapq.heappush(heap, (-dictionary[key], key))
        print(heap)
        res = []
        for _ in range(k):
            val = heapq.heappop(heap)
            res.append(val[1])

        return res