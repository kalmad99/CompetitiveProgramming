import heapq


class Solution:
    def topKFrequent(self, words, k: int):
        dictionary = {}
        for word in words:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
        heap = []
        for key in dictionary:
            heapq.heappush(heap, (-dictionary[key], key))
        print(heap)
        res = []
        for _ in range(k):
            val = heapq.heappop(heap)
            res.append(val[1])

        return res