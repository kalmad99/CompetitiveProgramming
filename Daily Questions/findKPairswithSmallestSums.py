import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        heap, res = [], []
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(heap, (nums1[i] + nums2[j], (nums1[i], nums2[j])))
        if k > len(nums1) * len(nums2):
            size = len(nums1) * len(nums2)
        else:
            size = k
        for _ in range(size):
            val = heapq.heappop(heap)
            res.append(val[1])
        return res
