import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        maxheap = []
        for i in stones:
            maxheap.append(-1 * i)
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            first = heapq.heappop(maxheap)
            second = heapq.heappop(maxheap)
            if first == second:
                continue
            else:
                heapq.heappush(maxheap, first - second)

        if len(maxheap) == 1:
            return maxheap[0] * -1
        else:
            return 0

sn = Solution()
print(sn.lastStoneWeight([2,7,4,1,8,1]))
